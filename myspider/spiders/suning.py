# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from myspider.items import SunningItem
import re
import urllib
import scrapy_redis
class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']
    def start_requests(self):
        cookies="_snvd=15557332146072NxtvZKJx3K; hm_guid=cd8c8a50-12f5-4f48-8c05-a053035eb390; _df_ud=6ef3082a-4477-4e5c-b947-3262b9a7cf0e; _device_session_id=p_dfe479f6-c763-4d31-a44a-fb8dc0b01b59; _cp_dt=5d170ddd-2b42-4e18-8164-a79d6a6021c7-39445; iar_sncd=0; tradeMA=95; custno=6095744607; idsLoginUserIdLastTime=; sncnstr=ydvmQTF3%2Bb%2B9ejwxnc%2FtmA%3D%3D; province=170; district=10001381; city=1000138; districtId=11107; provinceCode=170; cityId=9138; streetCode=7120199; districtCode=01; cityCode=712; SN_CITY=170_712_1000138_9138_01_11107_1_1_99_7120199; smhst=104879506|0070153176a10986592680|0070700749a136902376|0070726642a143085788|0070238264a11453461778|0070175047a11191427645|0070852352a11453995838|0070926447a11421455118|0070418556a650569594|0070167435a167223456|0070129646a11285056543|0070916356a11181302470|0070847914a11556828688|0070129646a11568195059|0070129646a655743610|0070167435a11327007047|0070847914a10082850184|0070138369a11321856631|0070129646a11407273339|0070153176a11306432034|0070916050; _snmc=1; _snzwt=THJDGJ1703899b82efbgha621; authId=si0182BE1CBB32FA5257A25E1C99779733; secureToken=AAED8827ECC0E3EB2CC54892A70C95D0; custLevel=161000000110; logonStatus=2; nick=%E6%98%8E%E5%90%8E%E5%A5%BD...; nick2=%E6%98%8E%E5%90%8E%E5%A5%BD...; _snsr=graph.qq.com%7Creferral%7C%7C%7C; route=1d565c0aadacec411060f1a6e7b80b12; _snma=1%7C158123070589841663%7C1581230705898%7C1581497605726%7C1581497633408%7C150%7C19; _snmp=158149763244285380; _snmb=158149760573644694%7C1581497633457%7C1581497633422%7C2"
        cookies = { i.split('=')[0]:i.split('=')[1] for i in cookies.split(';')}
        yield scrapy.Request(
            self.start_urls[0],
            callback = self.parse,
            cookies=cookies
            )
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
            #item['url']="https:"+li.xpath('''.//div[@class='img-block']/a/@href''').extract_first()
            item['url']=urllib.parse.urljoin(response.url,li.xpath('''.//div[@class='img-block']/a/@href''').extract_first())
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
            if(len(re.findall('''"itemPrice":"(.*?)",''',response.body.decode()))>0):
                item['price']=float(re.findall('''"itemPrice":"(.*?)",''',response.body.decode())[0])
                item['tittle']=response.xpath('''//*[@id="itemDisplayName"]/text()''')[-1].extract().strip()
                yield item
        
                
