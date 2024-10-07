from selenium import webdriver

def launchBrower():
    browser = webdriver.Chrome(service=service(chromẻiverManager().install()))
    browser.get("https://www.facebook.com/")
    return browser