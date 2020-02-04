import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service = Service('D:\Program Files\chromedriver_win32\chromedriver.exe')
#service.start()
#driver = webdriver.Remote(service.service_url)
path="D:\Program Files\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(executable_path=path)

driver.get('http://www.douban.com/')
myiframe=driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to_frame(myiframe)   ## �л�iframe�ӿ��
driver.maximize_window() 
driver.find_element_by_css_selector('li.account-tab-account').click()  # ��������¼�ı�ǩ
driver.find_element_by_id("username").send_keys("a1249812431@gmail.com")
driver.find_element_by_id("password").send_keys("chen1517")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/p[2]/label").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[5]/a").click()
cookies = {i['name']: i['value'] for i in driver.get_cookies()}
time.sleep(5) # Let the user actually see something!
driver.quit()