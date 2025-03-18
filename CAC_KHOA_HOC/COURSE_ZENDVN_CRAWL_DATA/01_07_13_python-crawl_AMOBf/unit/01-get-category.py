import requests
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="password",
    database="python_crawl"
)

create_table_sql = """ CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    link VARCHAR(255)
) """

cursor = mydb.cursor()
cursor.execute(create_table_sql)
mydb.commit()

url = 'http://demo-php-bookstore.zendvn.com/index.html'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
category_one = soup.select_one('#main-menu > li:nth-child(4) > ul > li:nth-child(6) > a')

items_category = soup.select('#main-menu > li:nth-child(4) > ul > li')

items_insert = []

for item in items_category:
    name = item.select_one('a').text
    link = item.select_one('a')['href']

    # sql = """ INSERT INTO categories (name, link) VALUES ("{}", "{}") """.format(name, link)

    # cursor.execute(sql)

    # sql  = """ INSERT INTO categories (name, link) VALUES (%s, %s) """
    # data = (name, link)
    # cursor.execute(sql, data)   

    # mydb.commit()

    items_insert.append((name, link))

sql = """ INSERT INTO categories (name, link) VALUES (%s, %s) """
cursor.executemany(sql, items_insert)
mydb.commit()

cursor.close()
mydb.close()

# print(category_one.text + "-----" + category_one.get('href'))