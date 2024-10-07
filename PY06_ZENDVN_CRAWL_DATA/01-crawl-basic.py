import requests
from bs4 import BeautifulSoup

url = 'http://demo-php-bookstore.zendvn.com/index.html'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
print(soup)
category_one = soup.select_one('#main-menu > li:nth-child(2) > ul > li:nth-child(1) > a')

print(category_one.text + "-----" + category_one.get('href'))