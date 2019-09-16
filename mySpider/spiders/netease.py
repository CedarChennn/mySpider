# -*- coding: utf-8 -*-
import scrapy
import copy


class NeteaseSpider(scrapy.Spider):
    name = 'netease'
    allowed_domains = ['163.com']
    start_urls = ['http://163.com/']

    def parse(self, response):
        item = {}
        #item["come_from"] = "netease"
        tittle = response.xpath('//*[@id="js_index2017_wrap"]/div[2]/div[2]/div[4]/div[1]/div[2]/div/div/div/div/div/div/ul/li/a/text()').extract_first()
        t = copy.deepcopy(tittle)
        print(tittle)

