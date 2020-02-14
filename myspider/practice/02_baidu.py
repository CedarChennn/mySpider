

#import requests
#import json
#headers = {"user - agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
#proxies = {"https":"https://119.142.78.39:9659"}
#url="https://www.baidu.com/"
##if __name__ == '__main__':
#r=requests.get(url,headers=headers)
#c=r.content.decode()
#print(r.status_code)
#print(c)

import requests
import datetime
post_url="https://byu.educationgroup.cn/wx/wxWjdc/save"
headers={"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1","cookie":"sid=1; surl=byu; SmartUserRole=portal; fwtj=%7B%22drzs%22%3A21081%2C%22zs%22%3A151980%7D; loginCode=7f367281bba91bd682d613522a67949a; Auth-Token=436fcccae70ecdb8c3fe0f43a961d843"}
data={"set_id": "byu{}".format(datetime.datetime.now().strftime('%m-%d').replace('-','')),
"da4edd2dd08a4bdeb37c294de48102d1":"家里",
"4fea40035dd44729a635b22943603dbb":"石花镇武当路87号",
"1844e9a145d640d29a4f5a40e737ca0e":"湖北",
"375e07ca2aa94ac8b140310b60b68d1f":"9D959E8182D51B3BE0530100007F5AE2",
"8fd7d4c8c5f3448b914b685fb5c3d40b":"无",
"1ebf98fdabeb4fb29235922bf07236a7": "无",
"d59e4136cc704169bfd3f736f411d77d": "无",
"28527b382b3c4ade855e2c6c6d19ce83": "9DBCD6CDE2D98EC4E0530100007F889A",
"11566aab8f3a441d93891d5c519dee01": "",
"56b935b53b8c43b1b0a0979b8bb1e765": "9D950E6640451AC1E0530100007FC5EF",
"f1765bc8eb9547f1a2bc9046ec121379": "",
"c17e1360d7864eaa90de9380dfddba69": "9DDDD08A6C394ADBE0530100007FB3DB",
"items": "4fea40035dd44729a635b22943603dbb,1844e9a145d640d29a4f5a40e737ca0e,375e07ca2aa94ac8b140310b60b68d1f,8fd7d4c8c5f3448b914b685fb5c3d40b,1ebf98fdabeb4fb29235922bf07236a7,d59e4136cc704169bfd3f736f411d77d,28527b382b3c4ade855e2c6c6d19ce83,11566aab8f3a441d93891d5c519dee01,56b935b53b8c43b1b0a0979b8bb1e765,f1765bc8eb9547f1a2bc9046ec121379,c17e1360d7864eaa90de9380dfddba69"}
r=requests.post(post_url,headers=headers,data=data)
print(datetime.datetime.now().strftime('%m-%d').replace('-','')+':'+str(r.status_code))

# 2月20的已经提交