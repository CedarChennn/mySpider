import requests
import json
import os
import sys
from lxml import etree
from pprint import pprint
headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1", "Cookie":"name=value; Hm_lvt_09f8618d1920d416f245832b6fcb87ae=1572173160,1572768833; name=value; ASP.NET_SessionId=yiqsr545bampiu45vaolg045",
           "Cookie":"TIEBAUID=7a4a7b31282d98755fa620b2; TIEBA_USERTYPE=f9630f1edde5aba971fc05b9; bdshare_firstime=1569156722197; BIDUPSID=4A32FF42B3BEE2291DA315CE737F9315; PSTM=1577276112; BAIDUID=4A32FF42B3BEE2298BCB772EFA7D0D79:FG=1; BDUSS=RHc0ZWZkRaWUFKejdafmJiQzVJclZuaUtpUFB1Tmp6THpOWWkteGNRN35xVTllRUFBQUFBJCQAAAAAAAAAAAEAAABe2i9is9jFz2ZvcmV2ZXIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP8cKF7~HCheM3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=138597_141144_100806_141661_139403_139110_135847_141000_139148_138471_140853_133994_138878_137979_140173_131247_132551_141261_138165_107313_138883_140259_141030_141367_140631_140201_139296_136862_138586_139174_139625_140113_136196_140590_140578_133847_140792_140065_140018_131423_140383_136537_136753_110085_131115_127969_140269_140593_140865_137253_140344_139409_128201_138313_138426_141194_138944_139677_141191_140596_140962; IS_NEW_USER=3b1b6fd7e34c04a84a971e75; BAIDU_WISE_UID=wapp_1580475795185_633; CLIENTHEIGHT=812; CLIENTWIDTH=375; STOKEN=dc19df24bcf2ba8fd1ccda3bbd43b431bc7535040f116100228347740b5f8700; recommend_item_click=0; pb_prompt=1; SET_PB_IMAGE_WIDTH=355; SEENKW=linux%23lol; mo_originid=2; USER_JUMP=-1; Hm_lvt_7d6994d7e4201dd18472dd1ef27e6217=1580475807,1580481517,1580481725; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1580475861,1580481525,1580481727; LASW=375; Hm_lpvt_7d6994d7e4201dd18472dd1ef27e6217=1580521724; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1580521992"}
url = "https://tieba.baidu.com/f?kw=广东白云学院&pn={}&"
p_url="https://tieba.baidu.com/mo/q/m?kw=linux&pn=0&lp=5024&forum_recommend=1&lm=0&cid=0&has_url_param=0&pn=120240&is_ajax=1"

for p in range(0,876):
    try:
        r=requests.get(url.format(p*30),headers=headers)
        html=etree.HTML(r.content.decode())
        for i in range(1,40):
                adtype=html.xpath('''//*[@id="frslistcontent"]/li[{}]/@class'''.format(i))
                if(len(adtype)==1 and len(adtype[0])==24):  ## filtering ads         
                    username=html.xpath('''//*[@id="frslistcontent"]/li[{}]/div/div[2]/div/span/text()'''.format(i))[0]
                    content=html.xpath('''//*[@id="frslistcontent"]/li[{}]/a/div[1]/span/text()'''.format(i))[0]
                    #url_list=html.xpath('''//img[@class='BDE_Image']/@src''')
                    #url_list=[requests.utils.unquote(url).split('src=')[-1] for url in url_list] # 获取源图片
                    with open('tieba.txt','a',encoding="utf-8") as f:
                        f.write(content+"\n")
                    #print(username+"***"+content)      
        print("loading number {}".format(p))
    except Exception as e:
        print(e.args)
