# -*- coding: utf-8 -*-
import scrapy
import logging
from myspider.items import MyspiderItem
logger = logging.getLogger(__name__)  # display the current spider name

class NeteaseSpider(scrapy.Spider):
    name = 'netease'
    allowed_domains = ['163.com']
    start_urls = ['https://news.163.com']

    def parse(self, response):
        item = MyspiderItem()
        tittle = response.xpath('//*[@id="js_origina_column"]/div/div/div/div/ul/li/div/ul/li/a/text()').extract()
        url= response.xpath('//*[@id="js_origina_column"]/div/div/div/div/ul/li/div/ul/li/a/@href').extract()
        for t in tittle:
            item['tittle'] = t           
        for u in url:
            item['url'] = u
            logger.warning(item)
        yield item