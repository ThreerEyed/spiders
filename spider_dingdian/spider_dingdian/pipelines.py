# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from spider_dingdian.items import SpiderQidianItem
from spider_dingdian.mysqlpipelines.sql import Sql


class SpiderQidianPipeline(object):
    def process_item(self, item, spider):
        # if isinstance(item, SpiderQidianItem):
        #     name_id = item['name_id']
        #     ret = Sql.select_name(name_id)
        #     if ret[0] == 1:
        #         print('已经存在了')
        #         pass
        #     else:
        #         xs_name = item['name']
        #         xs_author = item['author']
        #         category = item['category']
        #         Sql.insert_xiaoshuo(xs_name, xs_author, category, name_id)
        #         print('开始下载小说标题')
        return item
