# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from myspider.items import SunningItem
import re
class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']
    def parse(self, response):
        div_list = response.xpath('''//div[@class='submenu-left']''')
        for div in div_list:       
            p_list = div.xpath('''./p[@class='submenu-item']''')
            for p in p_list:
                item=SunningItem()
                item['big_cate']=p.xpath('./a/text()').extract_first()
                for i in p.xpath('''./following-sibling::*[1]/li/a'''):
                    item=deepcopy(item)
                    item['small_cate']=i.xpath('./text()').extract_first()
                    yield scrapy.Request(
                        i.xpath('''./@href''').extract_first(),
                        callback=self.parse_page,
                        meta={"item":item}
                        )
    def parse_page(self,response):
        li_list=response.xpath('''//ul[@class="clearfix"]/li''')
        for li in li_list:
            item = deepcopy(response.meta["item"])
            item['url']="https:"+li.xpath('''.//div[@class='img-block']/a/@href''').extract_first()
            yield scrapy.Request(
            item['url'],
            callback=self.parse_book,
            meta={"item":item}
            )
            page_number=int(re.findall('''共(.*?)页''',response.body.decode())[0])
            ci=re.findall('''-(.*?)-''',response.request.url)[0]
            for i in range(1,page_number):
                item = deepcopy(response.meta["item"])
                item['url']='''https://list.suning.com/emall/showProductList.do?ci={}&pg=03&cp={}&il=0&iy=0&adNumber=0&n=1&ch=4&prune=0&sesab=ACBAABC&id=IDENTIFYING&cc=025'''.format(ci,i)
                yield scrapy.Request(
                item['url'],
                callback=self.parse_next_page,
                meta={"item":item}                    
                )
                item['url']='''https://list.suning.com/emall/showProductList.do?ci={}&pg=03&cp={}&il=0&iy=0&adNumber=0&n=1&ch=4&prune=0&sesab=ACBAABC&id=IDENTIFYING&cc=025&paging=1&sub=0'''.format(ci,i)
                yield scrapy.Request(
                item['url'],
                callback=self.parse_next_page,
                meta={"item":item}
                )
        
    def parse_next_page(self,response):      
        div_list = response.xpath('''//div[contains(@class,'img-block')]''')
        for div in div_list:
            item = deepcopy(response.meta["item"])
            item['url']= "https:"+div.xpath('''./a/@href''').extract_first()
            yield scrapy.Request(
                item['url'],
                callback=self.parse_book,
                meta={"item":item}
                )
       
    def parse_book(self,response):   
        item = response.meta["item"]
        item['price']=float(re.findall('''"itemPrice":"(.*?)",''',response.body.decode())[0])
        item['tittle']=response.xpath('''//*[@id="itemDisplayName"]/text()''')[-1].extract().strip()
        yield item
        
                
