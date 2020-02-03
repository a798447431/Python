# -*- coding: utf-8 -*-
import scrapy
from chinanews_crawl.items import ChinanewsCrawlItem

class ChinanewsSpider(scrapy.Spider):
    name = 'chinanews'
    allowed_domains = ['chinanews.com']
    start_urls = ['http://www.chinanews.com/rss/scroll-news.xml']
    
    def start_request(self):
        yield scrapy.Requset(url = self.start_urls, callback = self.parse)
    
    def parse(self, response):
        news_list = response.xpath('//rss/channel/item')
        for i in news_list:
            title = i.xpath('./title/text()').extract()
            url = i.xpath('./link/text()').extract()[0]
            description = i.xpath('./description/text()').extract()
            yield scrapy.Request(url , meta = {"title" : title, "url" : url, "description" : description}, callback = self.parse1)

    def parse1(self, response):
        news = ChinanewsCrawlItem()
        content = response.xpath('//*[@id="cont_1_1_2"]/div[6]/p/text()')
        news['title'] = response.meta["title"]
        news['url'] = response.meta["url"]
        news['description'] = response.meta["description"]
        news['content'] = content
        yield news

