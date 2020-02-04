# -*- coding: utf-8 -*-
import scrapy
import logging
# https://www.jianshu.com/p/0a5f36b7dcff
class CountrySpider(scrapy.Spider):
    name = 'country'
    allowed_domains = ['country-code.cl']
    start_urls = ['https://country-code.cl']

    def parse(self, response):
    # //*[@id="row0"]/td[1]
    # //*[@id="row0"]/td[3]/span[3]
    # //*[@id="row0"]/td[4]/a/text()
        countrylist=response.xpath('//*[starts-with(@id,"row")]')
        for country in countrylist:
            item={}
            item['continent']=country.xpath('./td[1]/text()').extract_first()
            item['country_name'] = country.xpath('./td[3]/span[3]/text()').extract_first()
            item['country_short_name']=country.xpath('./td[4]/a/text()').extract_first()
            item['url']=country.xpath('./td[2]/a/img/@src').extract_first()      
            yield item