# -*- coding: utf-8 -*-
import scrapy
import re

class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        utf8 = response.xpath("//input[@name='utf8']/@value").extract_first()
        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        post_data = dict(
            login="a124gmail.com",
            password="Cch498",
            authenticity_token=authenticity_token,
            utf8=utf8,
            commit=commit
        )
        yield scrapy.FormRequest(
            "https://github.com/session",
            formdata=post_data,
            callback=self.after_login
        )

    def after_login(self,response):
        #with open("a.html","w",encoding="utf-8") as f:
        #     f.write(response.body.decode())
  
        print(re.findall("study",response.body.decode()))

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, #自动的从response中寻找from表单
            formdata={"login":"agmail.com","password":"C8"},
            callback = self.after_login
        )

    def after_login(self,response):
        with open("a.html","w",encoding="utf-8") as f:
             f.write(response.body.decode())
        print(re.findall("CedarChennn",response.body.decode()))
        print('*'*48)


