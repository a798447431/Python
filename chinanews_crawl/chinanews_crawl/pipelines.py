# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from chinanews_crawl import settings 

class ChinanewsCrawlPipeline(object):
    def open_spider(self, spider):
        self.file = open(settings.STORE+'/'+'test.txt', 'w')
    def process_item(self, item, spider):
        content = str(item['content']) + "\n"
        self.file.write(content)
        return item
    def close_spider(self, spider):
        self.file.close()
