# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem
from pprint import pprint
from datetime import datetime
import json
class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=']

    def parse(self, response):    
        tr_list=response.xpath(r'/html/body/div[8]/table[2]/tr')
        for tr in tr_list:
            item=MyspiderItem()
            item['id']=int(tr.xpath('./td[1]/text()').extract_first())
            item['tittle']=tr.xpath('./td[3]/a[1]/text()').extract_first()
            item['href']=tr.xpath('./td[3]/a[1]/@href').extract_first()
            item['name']=tr.xpath('./td[5]/text()').extract_first()
            item['publish_date']=str(datetime.strptime(tr.xpath('./td[6]/text()').extract_first(), '%Y-%m-%d %H:%M:%S') ) 
            item['question_detail']=""
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={'item':item}
                )
            # //div[@class='pagination']/a[text()='>']

        next_url=response.xpath('''/html/body/div[9]/div/a[text()='>']/@href''').extract_first()
        if next_url is not None:
        #if next_url != 'http://wz.sun0769.com/index.php/question/report?page=60':
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                )
    def parse_detail(self, response):
        item=response.meta['item']
        for i in response.xpath('/html/body/div[9]/table[2]/tr[1]/td'):
            if (i is not None):
                item['question_detail']+=i.xpath('./text()').extract_first()

        pprint(item['publish_date'])
       # print(type()
        with open("sun.json",'a',encoding="utf-8") as f:
            f.write(json.dumps(dict(item),ensure_ascii=False,indent=4))
        yield item

