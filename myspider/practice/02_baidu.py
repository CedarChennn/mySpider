

import requests
import json
headers = {"user - agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
proxies = {"https":"https://119.142.78.39:9659"}
url="https://www.baidu.com/"
#if __name__ == '__main__':
r=requests.get(url,headers=headers)
c=r.content.decode()
print(r.status_code)
print(c)