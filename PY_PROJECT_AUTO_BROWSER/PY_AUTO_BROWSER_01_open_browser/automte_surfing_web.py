from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options to block notifications
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Function to launch the browser
def launchBrowser():
    # Set up the Chrome WebDriver
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    # Open the initial webpage
    browser.get("https://www.vnexpress.net/")
    return browser

# Launch the browser
browser = launchBrowser()
time.sleep(15)

# Open the new link
browser.get("https://kenh14.vn/")
time.sleep(15)