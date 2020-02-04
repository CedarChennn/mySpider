import requests
import json
import os
import sys
#if __name__ == '__main__':
cookie="anonymid=k5xlua91cp5e8y; depovince=ZGQT; _r01_=1; JSESSIONID=abcn62mf0xRSxdXDZnR-w; ick_login=09b779d0-8e26-4ada-a67c-5317b15e40db; taihe_bi_sdk_uid=aaa9ba5a3292144eb14a2f4ab2aa08b3; taihe_bi_sdk_session=6fadcb79069458f69c410a3da0fb6bb9; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20190326/0930/main_V1St_81d40000bf431986.jpg; jebe_key=5bb2042d-9f4a-4ff1-b068-793e4f90b2a6%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1580199289101%7C1%7C1580199288781; wp_fold=0; jebecookies=548f881b-f813-4d8b-8ac7-cc93c7eaf854|||||; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=71018311dcabdd8c52eceb805c43c0649; ap=327550029; t=6e3cd902d54032d99eb074f3171c5b989; societyguester=6e3cd902d54032d99eb074f3171c5b989; id=327550029; xnsid=14bd5638; ver=7.0; loginfrom=null"
#cookies= { i.split("=")[0]:i.split("=")[1] for i in cookie.split(";")} 
headers = {"user - agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           "cookie":cookie}
proxies = {"https":"https://119.142.78.39:9659"}
session=requests.session()
post_data={"email":"mr_mao_hacker@163.com","password":"Aalarmchime"}
post_url="http://www.renren.com/PLogin.do"
url="http://www.renren.com/327550029/newsfeed/photo"
#使用session发送post请求，吧cookie保存在其中
#session.post(url,data=post_data,headers=headers)
#r=session.get(url,headers=headers)
r=requests.get("http://www.renren.com/327550029/newsfeed/photo",headers=headers)  #headers加上cookie
c=r.content.decode()
with open("renren.html",'w+',encoding="utf8") as f:
    f.write(c)
print(sys.argv[0])
print(sys.argv[1])