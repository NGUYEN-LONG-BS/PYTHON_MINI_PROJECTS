# ======================================================================================
# Dowloading dữ liệu từ web với Request
# Lưu file ở path hiện hành
# ======================================================================================


# Used to import the webdriver from selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
# Get the path of chromedriver which you have install 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
chrome_options = Options()

import time

path = "D:\89.Vm\17. Login_Auto\01. Ex\chromedriver.exe" 
ser = Service(path)
# giving the path of chromedriver to selenium webdriver 
browser = webdriver.Chrome (service= ser)

# opening the website in chrome. 
browser.get("https://batdongsan.com.vn/nha-dat-ban")

browser.maximize_window()
time.sleep(40)