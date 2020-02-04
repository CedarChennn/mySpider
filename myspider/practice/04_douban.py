import requests
import json
import os
import sys
from pprint import pprint
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=1000&page_start=0"
#ʹ��session����post���󣬰�cookie����������
#session.post(url,data=post_data,headers=headers)
#r=session.get(url,headers=headers)
r=requests.get(url,headers=headers)  #headers����cookie
c=r.content.decode()
c=json.loads(c)  # json to dict
count=0
for i in c['subjects']:
    print(str(count)+":"+i['title'])
    count+=1
#pprint(c)
with open("douban.json",'w',encoding="utf-8") as f:
    f.write(json.dumps(c,ensure_ascii=False,indent=4))
