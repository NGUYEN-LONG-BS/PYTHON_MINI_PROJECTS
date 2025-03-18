import requests
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="password",
    database="python_crawl"
)

create_table_sql = """ CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    link VARCHAR(255),
    image_link VARCHAR(255),
    price_current VARCHAR(255),
    price_old VARCHAR(255),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
) """


cursor = mydb.cursor()
cursor.execute(create_table_sql)
mydb.commit()

def get_products_in_category(category_url, category_id):    
    max_page = 100
    items_insert = []

    for i in range(max_page):
        page_url = f"{category_url}?page={i+1}"

        html = requests.get(page_url).text
        soup = BeautifulSoup(html, 'html.parser')

        items_product = soup.select(".product-box")

        if not items_product:
            break

        for item in items_product:
            name = item.select_one('.product-name').text
            link = item.select_one('.product-link')['href']
            image_link = item.select_one('.img-fluid')['src']
            price_old_element = item.select_one('.text-lowercase > del')
            price_old = price_old_element.text if price_old_element else None
            price_current = item.select_one('.text-lowercase').text
            price_current = price_current.replace(price_old, "").strip() if price_old_element else price_current

            items_insert.append((name, link, image_link, price_current, price_old, category_id))

    sql = """ INSERT INTO products (name, link, image_link, price_current, price_old, category_id) VALUES (%s, %s, %s, %s, %s, %s) """
    cursor.executemany(sql, items_insert)
    mydb.commit()

category_url = 'http://demo-php-bookstore.zendvn.com/cong-nghe-thong-tin-3.html'
category_id  = 3

get_products_in_category(category_url, category_id)

cursor.close()
mydb.close()