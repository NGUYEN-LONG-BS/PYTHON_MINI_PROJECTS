from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


from selenium.webdriver.chrome.options import Options

# Set up Chrome options to block notifications
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Set up the Chrome WebDriver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


# pip install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager

def launchBrower():
    # Set up the Chrome WebDriver
    # browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    # Open Facebook login page
    browser.get("https://www.facebook.com/")
    return browser

brower = launchBrower()
# brower.maximize_window()

time.sleep(5)

# user_name = brower.find_element(By.ID, "email").send_keyS("phamxuananx1@gmail.com")
# Find the email input field and enter the email
user_name = brower.find_element(By.ID, "email")
user_name.send_keys("nguyenlongbshop@gmail.com")

# pass_word = brower.find_element(By.ID, "pass").send_keyS("123456#111")
pass_word = brower.find_element(By.ID, "pass")
pass_word.send_keys("pn310716long")

login_user = brower.find_element(By.NAME, "login").click()

time.sleep(60)

login_user = brower.find_element(By.NAME, "Tin cậy thiết bị này").click()

time.sleep(60)