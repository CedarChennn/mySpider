import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import json
class Douyu:
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = driver=webdriver.Chrome(executable_path="D:\Program Files\chromedriver_win32\chromedriver.exe")
        self.js="var q=document.documentElement.scrollTop=10000"
        

    def get_content_list(self):
        li_list=self.driver.find_elements_by_xpath('''//*[@id="listAll"]/section[2]/div[2]/ul/li''')  
        content_list=[]
        for li in li_list:
            item={}
            item["room_host_name"]=li.find_element_by_xpath('''./div/a[1]/div[2]/div[2]/h2''').text
            room_hot_number=li.find_element_by_xpath('''./div/a[1]/div[2]/div[2]/span''').text
            if(room_hot_number[-1] != '万'):
                item["room_hot_number"]=int(room_hot_number)
            else:
                room_hot_number=room_hot_number[0:-1]
                if(len(room_hot_number.split('.'))==1):
                    item["room_hot_number"]=int(room_hot_number)*10000
                else:
                    item["room_hot_number"]=int(room_hot_number.split('.')[0])*10000+int(room_hot_number.split('.')[1])*10000/len(room_hot_number.split('.')[1])
            item["tittle"]=li.find_element_by_xpath('''./div/a[1]/div[2]/div[1]/h3''').text
            item["room_cate"]=li.find_element_by_xpath('''./div/a[1]/div[2]/div[1]/span''').text
            item["room_url"]=li.find_element_by_xpath('''./div/a[1]''').get_attribute("href")
            content_list.append(item)
        next_url=self.driver.find_elements_by_xpath('''//*[@id="listAll"]/section[2]/div[2]/div/ul/li/span''')

        next_url=next_url[-1] if len(next_url)>0 else None
        return content_list,next_url
    def save_content_list(self,content_list):
        print(content_list)
        with open("douyu.json",'a',encoding="utf-8") as f:
            f.write(json.dumps(content_list,ensure_ascii=False,indent=4))

    def run(self):
        self.driver.get(self.start_url)
        self.driver.maximize_window() 
        content_list,next_url=self.get_content_list()
        self.save_content_list(content_list)
        while next_url.get_attribute("class") !="dy-Pagination-disabled dy-Pagination-next":
            next_url.click()          
            time.sleep(3)
            self.driver.execute_script(self.js)
            time.sleep(3)
            content_list,next_url=self.get_content_list()
            self.save_content_list(content_list)
if __name__=="__main__":
    douyu =Douyu()
    douyu.run()

