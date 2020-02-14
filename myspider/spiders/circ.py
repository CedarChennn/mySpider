# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class CircSpider(CrawlSpider):
    name = 'circ'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://circ.gov.cn/web/site0/tab5240/']

    rules = (
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'), callback='parse_item',),
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/module14430/page\d+\.htm'),callback='parse_item1', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        a=re.findall("(身份证号：.*?)</p>",response.body.decode())
        if(len(a)>0):
            item['name'] = a[0]
            #item['name']=response.xpath('''//*[@id="zoom"]/p[5]/text()''').extract_first().split('：')[-1]
            print(item)
            return item
    def parse_item1(self, response):
        item = {}
        print(response.request.url)
        return item

