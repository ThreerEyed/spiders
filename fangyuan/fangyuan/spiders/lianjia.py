
import scrapy
from scrapy import Selector, Request

from fangyuan.items import FangyuanItem


class LianJiaSpider(scrapy.Spider):

    name = 'lianjia'
    start_urls = ['https://cd.zu.ke.com/zufang']

    def parse(self, response):
        sel = Selector(response)
        all_area = sel.xpath('//ul[@data-target="area"]/li/a')[1:]
        for area in all_area:
            area_name = area.xpath('./text()').extract()[0]
            url = area.xpath('./@href').extract()[0]
            area_url = self.start_urls[0] + url[url.find('g/') + 1:]

            return Request(area_url, callback=self.get_all_page, meta={'area_name': area_name})

    def get_all_page(self, response):
        sel = Selector(response)

        total_page = sel.xpath('//div[@class="content__pg"]/@data-totalpage').extract()[0]
        for i in range(int(total_page)):
            every_page_url = response.url + str(i)
            area_name = response.meta.get('area_name')

            return Request(every_page_url, callback=self.get_house_url,
                           meta={'area_name': area_name})

    def get_house_url(self, response):
        """拿到页面的每一个div 中的房屋信息"""
        sel = Selector(response)

        all_div = sel.xpath('//*[@id="content"]/div[1]/div[1]/div')
        for i in all_div:

            house_url =i.xpath('./a[1]/@href').extract()[0]
            area_name = response.meta.get('area_name')
            # house_index_image = i.xpath('./a[2]/img/@src').extract()[0]
            return Request(self.start_urls[0] + house_url[house_url.find('g/') + 1:],
                           callback=self.get_house_info,
                           meta={'area_name': area_name})

    def get_house_info(self, response):
        """得到房源各种信息"""
        sel = Selector(response)
        item = FangyuanItem()

        item['house_name'] = sel.xpath('/html/body/div[3]/div[1]/div[3]/p[1]/text()').extract()[0]
        item['house_area'] = response.meta.get('area_name')
        item['house_size'] = sel.xpath('//*[@id="aside"]/p[3]/span[3]/text()').extract()[0]
        item['house_head'] = sel.xpath('//*[@id="aside"]/p[3]/span[4]/text()').extract()[0]
        item['house_style'] = sel.xpath('//*[@id="aside"]/p[3]/span[2]/text()').extract()[0]
        item['house_data_from'] = sel.xpath('//*[@id="aside"]/ul/li/p[2]/text()').extract()[0].strip()
        item['house_create_time'] = sel.xpath('/html/body/div[3]/div[1]/div[3]/p[2]/text()').extract()[0]
        item['house_price'] = sel.xpath('//*[@id="aside"]/p[1]/span/text()').extract()[0]
        item['house_info'] = sel.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[2]/ul/li/text()').extract()[0]
        item['house_describle'] = sel.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/ul/li/text()').extract()[0]

        return item








