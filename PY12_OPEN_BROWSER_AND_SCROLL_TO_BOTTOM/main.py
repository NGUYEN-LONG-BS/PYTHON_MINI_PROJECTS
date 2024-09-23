# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (make sure the path to your WebDriver is correct)
# driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
#  driver = webdriver.Chrome(ChromeDriverManager().install())
# webdriver.Chrome()
# C:\Users\ADMIN\Desktop\chrome-win64\chrome-win64

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# Open a webpage
driver.get('https://www.example.com')

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Wait for a few seconds to see the result
time.sleep(5)

# Close the browser
driver.quit()
