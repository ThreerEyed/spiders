import re
import scrapy
from bs4 import BeautifulSoup
from scrapy import Selector
from scrapy.http import Request

from spider_dingdian.items import SpiderQidianItem, ContentItem


class MySpider(scrapy.spiders.Spider):

    # name 是我们在要调用时候的名称
    name = 'dingdian'
    # 允许的域名
    allowed_domains = ['23us.so']
    # 每一个菜单的地址前缀
    bash_url = 'http://www.23us.so/list/'

    def start_requests(self):
        # 循环总共的分类
        for i in range(1, 10):
            # 粘贴url全路径
            url = self.bash_url + str(i) + '_1.html'
            # 我们使用了导入的Request包，来跟进我们的URL
            # （并将返回的response作为参数传递给self.parse,
            yield Request(url, self.parse)
        # 全本小说
        yield Request('http://www.23us.so/full.html', self.parse)

    # 定义函数处理我们得到的分类的所有url
    def parse(self, response):
        # 找到最大的网页数
        max_num = BeautifulSoup(response.text, 'lxml').find('div', class_='pagelink').find_all('a')[-1].get_text()
        # 通过循环拿到我们的url 并通过yield 保存我们的url yield 在此处有协程的作用
        base_url = response.url[:-6]
        for i in range(int(max_num) + 1):
            page_url = base_url + str(i) + '.html'
            yield Request(page_url, callback=self.get_page)

    # 定义函数处理我们拿到的每一页的url
    def get_page(self, response):
        # 找到所有的小说的信息, 找到的一个列表
        tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
        # 循环所有的tds 拿到我们每一个小说的相关信息, 拿到对应的小说名和url
        for td in tds:
            novel_name = td.find('a').get_text()
            novel_url = td.find('a')['href']
            # 然后拿到一次就传递给我们定义的get_chapter 来处理, 指定的meta 可以作为参数传递给我们回调函数
            yield Request(novel_url, callback=self.get_chapter_info, meta={'name': novel_name,
                                                                           'url': novel_url})

    def get_chapter_info(self, response):
        # 使用beautifulsoup 解析页面, 拉到我们的soup 对象
        soup = BeautifulSoup(response.text, 'lxml')
        # 实例化我们的item 对象, 用来保存我们相关数据的值
        item = SpiderQidianItem()
        # 小说名
        item['name'] = response.meta['name']
        # 小说作者
        item['author'] = soup.find('table').find_all('td')[1].get_text().replace('\xa0', '')
        # 小说目前连载状态
        item['status'] = soup.find('table').find_all('td')[2].get_text().replace('\xa0', '')
        # 小说目前连载总字数
        item['current_world_count'] = soup.find('table').find_all('td')[4].get_text().replace('\xa0', '')
        # 小说总点击数
        item['current_click_count'] = soup.find('table').find_all('td')[6].get_text().replace('\xa0', '')
        # 小说最后更新时间
        item['last_update_time'] = soup.find('table').find_all('td')[5].get_text().replace('\xa0', '')
        # 小说目录
        item['category'] = soup.find('table').find_all('td')[0].get_text().replace('\xa0', '')
        # 小说内容介绍
        item['content_introduction'] = soup.find('dd', style="padding:10px 30px 0 25px;").find_all('p')[1].get_text().strip()
        name_id = response.url[response.url.rfind('/') + 1:-5]
        item['name_id'] = name_id
        sel = Selector(response)
        detail_url = sel.xpath('//a[@class="hst"]/@href').extract()[0]
        # 将我们的item 返回
        yield item
        yield Request(detail_url, callback=self.get_chapter, meta={'name_id': name_id})

    def get_chapter(self, response):
        """
        拿到小说章节信息
        :param response:
        :return:
        """
        info_list = re.findall('<td class="L".*?href="(.*?)">(.*?)</a>', response.text)
        num = 0
        for td in info_list:
            num += 1
            chapter_url = td[0]
            name_id = response.meta.get('name_id')

            yield Request(chapter_url, callback=self.get_content,
                           meta={'num': num, 'name_id': name_id})

    def get_content(self, response):
        sel = Selector(response)
        item = ContentItem()
        item['name_id'] = response.meta.get('name_id')
        item['chapter_name'] = sel.xpath('//*[@id="amain"]/dl/dd[1]/h1/text()').extract()[0]
        item['num'] = response.meta.get('num')
        item['chapter_url'] = response.url
        content = sel.xpath('//*[@id="contents"]').extract()[0].replace('\xa0', '')
        item['content'] = content.replace('<br>', '')[17:]

        yield item

