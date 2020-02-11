# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymysql
import requests
import re
logger = logging.getLogger(__name__)

class MyspiderPipeline(object):
    def __init__(self):    
        # 可选实现，做参数初始化等
        # doing something
        self.count=1
    def process_item(self, item, spider):  # 不return的情况下另一个权重较低的pipline就不会获取到该item
        # item (Item 对象) – 被爬取的item
        # spider (Spider 对象) – 爬取该item的spider
        # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
        # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
        
        if spider.name=='suning':
            values = (
                self.count,
                item['tittle'],
                item['price'],
                item['small_cate'],
                item['big_cate'],
                item['url']
                 )
            sql = 'INSERT INTO suning_book (id,tittle,price,small_cate,big_cate,url) VALUES(%s,%s,%s,%s,%s,%s)'
            self.db_cur.execute(sql, values)
            print(self.count)
            self.count+=1
            return item
        if spider.name=='country':
            item['country_short_name']=item['country_short_name'].split()[0]
            continent={"AF":1,"AN":2,"AS":3,"OC":4,"EU":5,"NA":6,"SA":7}
            values = (
            item['country_name'],
            item['country_short_name'],
            continent[item['continent']],
        )
            continent={"AF":1,"AN":2,"AS":3,"OC":4,"EU":5,"NA":6,"SA":7}
            sql = 'INSERT INTO universitylist_country (name,short_name,continent_id) VALUES(%s,%s,%s)'
            self.db_cur.execute(sql, values)
            r = requests.get(item['url'], stream=True)
            if r.status_code == 200:
                open('D:\\OneDrive\\github\\studyabroadapplication\\common_static\\img\\flag\\%s.jpg' % (item['country_name']), 'wb+').write(r.content)
        return item
        if spider.name=='netease':
            logger.warning("************")
            print('fuck')
        if spider.name=='sun':
            print('88888888888888888888')
            values = (
            item['id'],
            item['tittle'],
            item['name'],
            item['href'],
            item['publish_date'],
            item['question_detail'],
        )
            item['question_detail']=self.process_detail(item['question_detail'])
            sql = 'INSERT INTO sun (id,tittle,name,href,publish_date,question_detail) VALUES(%s,%s,%s,%s,%s,%s)'
        return item
    def process_detail(self, detail):
        detail = [re.sub(r"\xa0|\s","",i) for i in detail] 
        detail = [i for i in detail if len(i)>0]
        return detail  #

    def open_spider(self, spider):
        # spider (Spider 对象) – 被开启的spider
        # 可选实现，当spider被开启时，这个方法被调用。
        #connection = pymysql.connect(host='localhost',  user='root',  password='123456', db='studyabroadapplication',    charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        db = spider.settings.get('MYSQL_DB_NAME','spider')
        host = spider.settings.get('MYSQL_HOST', 'localhost')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', '123456')

        self.db_conn =pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()

    def close_spider(self, spider):
        # spider (Spider 对象) – 被关闭的spider
        # 可选实现，当spider被关闭时，这个方法被调用
        self.db_conn.commit()
        self.db_conn.close()

class MyspiderPipeline_add(object):
    def __init__(self):    
        # 可选实现，做参数初始化等
        # doing something
        pass
    def process_item(self, item, spider):
        # item (Item 对象) – 被爬取的item
        # spider (Spider 对象) – 爬取该item的spider
        # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
        # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
           
        return item