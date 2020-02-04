import requests
import json
headers = {"user - agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
data = {"client": "webapp",
"sl": "zh-CN",
"tl":"en",
"hl": "en",
"dt": "at",
"dt": "bd",
"dt": "ex",
"dt": "ld",
"dt": "md",
"dt": "qca",
"q": "你今天吃饭了吗"}
url="https://translate.google.cn/translate_a/single?client=webapp&sl=zh-CN&tl=en&hl=en"
if __name__ == '__main__':
    r=requests.get(url,headers=headers,data=data)
    c=r.content.decode()
    print(r.status_code)
