# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangyuanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 房屋名称
    house_name = scrapy.Field()
    # 房源区域
    house_area = scrapy.Field()
    # 房源大小
    house_size = scrapy.Field()
    # 房源朝向
    house_head = scrapy.Field()
    # 房屋类型
    house_style = scrapy.Field()
    # 数据来源
    house_data_from = scrapy.Field()
    # 房源发布时间
    house_create_time = scrapy.Field()
    # 房源价格
    house_price = scrapy.Field()
    # 房源基本信息
    house_info = scrapy.Field()
    # 房源配套设施
    house_facility = scrapy.Field()
    # 房源描述
    house_describle = scrapy.Field()
    # 房源中介联系方式
    house_contact_phone = scrapy.Field()
