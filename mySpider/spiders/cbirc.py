# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class CbircSpider(CrawlSpider):
    name = 'cbirc'
    allowed_domains = ['cbirc.gov.cn']
    start_urls = ['http://www.cbirc.gov.cn/cn/list/9103/910305/ybjhcf/1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/cn/doc/9103/910305/ybjhcf/\S+\.html'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = {}
        item["come_from"] = "cbirc"
        item['company'] = response.xpath('/html/body/table[2]/tbody/tr[2]/td/table/tbody/tr[3]/td/div/p[5]/span/text()').get()
        item['date'] = re.findall('''<td width="68%" height="56" align="center" valign="middle" class="t5">(.*?)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 文章来源：财险部(再保部)</td>''',response.body.decode())
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        print(item)
        return item
