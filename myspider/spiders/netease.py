# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)  # display the current spider name

class NeteaseSpider(scrapy.Spider):
    name = 'netease'
    allowed_domains = ['163.com']
    start_urls = ['https://news.163.com']

    def parse(self, response):
        item = {}
        tittle = response.xpath('//*[@id="js_origina_column"]/div/div/div/div/ul/li/div/ul/li/a/text()').extract()
        href= response.xpath('//*[@id="js_origina_column"]/div/div/div/div/ul/li/div/ul/li/a/@href').extract()
        for t in tittle:
            item['tittle'] = t
            print(type(t))
            print(item)
        for h in href:
            item['href'] = h
            print(h)
        yield item