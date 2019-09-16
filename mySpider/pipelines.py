# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
class MyspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "netease":
            print(item)
        elif spider.name == "cbirc":
            pass
        return item

    def open_spider(self,spider):  # 在爬虫开启的时候执行，仅执行一次
        self.file = open(spider.setting.get("SAVE_FILE","./temp/json"),'w')
    def close_spider(self,spider):
        self.file.close()

