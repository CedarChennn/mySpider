import requests
import json
import os
import sys
from pprint import pprint
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36", "Cookie":"name=value; Hm_lvt_09f8618d1920d416f245832b6fcb87ae=1572173160,1572768833; name=value; ASP.NET_SessionId=yiqsr545bampiu45vaolg045"}
url = "http://jwgl.baiyunu.edu.cn/xscj/Stu_MyScore_rpt.aspx"
data = {"SJ":"1",
"btn_search":"%BC%EC%CB%F7",
"SelXNXQ":"0",
"zfx_flag": "0",
"zxf": "0"}
r = requests.post(url,headers=headers,data=data)  #headers加上cookie
with open('jwgl.html','w',encoding='gb2312') as f:
    f.write(r.content.decode('gb2312'))
#pprint(r.content.decode())