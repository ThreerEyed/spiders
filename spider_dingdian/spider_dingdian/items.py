# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderQidianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name_id = scrapy.Field()
    # 小说姓名
    name = scrapy.Field()
    # 小说作者
    author = scrapy.Field()
    # 小说状态
    status = scrapy.Field()
    # 目前总字数
    current_world_count = scrapy.Field()
    # 总点击数
    current_click_count = scrapy.Field()
    # 最后更新时间
    last_update_time = scrapy.Field()
    # 小说类别
    category = scrapy.Field()
    # 内容简介
    content_introduction = scrapy.Field()


class ContentItem(scrapy.Item):

    # 小说id
    name_id = scrapy.Field()
    # 小说章节内容
    content = scrapy.Field()
    # 小说章节标题
    chapter_name = scrapy.Field()
    # 章节URL
    chapter_url = scrapy.Field()
    # 章节顺序
    num = scrapy.Field()




