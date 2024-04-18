from time import time

from selenium import webdriver


wd = webdriver.Chrome()
wd.get("https://www.baidu.com")    # 打开百度浏览器

time.sleep(3)   #等待3秒
wd.quit()   #关闭浏览器