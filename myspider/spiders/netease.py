# -*- coding: utf-8 -*-
import scrapy


class NeteaseSpider(scrapy.Spider):
    name = 'netease'
    allowed_domains = ['163.com']
    start_urls = ['http://163.com/']

    def parse(self, response):
        pass
