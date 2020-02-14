# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SunningItem(scrapy.Item):
    # define the fields for your item here like:
    big_cate = scrapy.Field()
    small_cate = scrapy.Field()
    url = scrapy.Field()
    tittle = scrapy.Field()
    price = scrapy.Field()
    publication_time = scrapy.Field()

class SunItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    country_name = scrapy.Field()
    country_short_name = scrapy.Field()
    continent = scrapy.Field()
    url = scrapy.Field()
    tittle = scrapy.Field()


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    tittle = scrapy.Field()
    href = scrapy.Field()
    url = scrapy.Field()
    status = scrapy.Field()
    name = scrapy.Field()
    publish_date = scrapy.Field()
    question_detail = scrapy.Field()
