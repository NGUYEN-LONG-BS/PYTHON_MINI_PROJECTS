# ======================================================================================
# Dowloading dữ liệu từ web với Request
# Lưu file ở path hiện hành
# ======================================================================================


# # Used to import the webdriver from selenium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options 
# # Get the path of chromedriver which you have install 
# from selenium.webdriver.chrome.service import Service 
# from selenium.webdriver.common.by import By
# chrome_options = Options()

# import time

# path = "D:\89.Vm\17. Login_Auto\01. Ex\chromedriver.exe" 
# ser = Service(path)
# # giving the path of chromedriver to selenium webdriver 
# browser = webdriver.Chrome (service= ser)

# # opening the website in chrome. 
# browser.get("https://batdongsan.com.vn/nha-dat-ban")

# browser.maximize_window()
# time.sleep(40)


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
# Automatically download and use the correct ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

# opening the website in chrome. 
driver.get("https://batdongsan.com.vn/nha-dat-ban")

driver.maximize_window()

try:
    # Locate and click "Not Allow" button
    not_allow_button = driver.find_element(By.XPATH, '//button[text()="Block"]')  # Adjust XPATH based on the website
    not_allow_button.click()
    print("Clicked 'Not Allow'")
except Exception as e:
    print("Notification not found or unable to interact:", e)

time.sleep(40)

print(driver.title)
driver.quit()
