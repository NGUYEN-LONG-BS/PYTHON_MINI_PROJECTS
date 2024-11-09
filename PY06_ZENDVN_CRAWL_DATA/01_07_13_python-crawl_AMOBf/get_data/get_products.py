import requests
from bs4 import BeautifulSoup
import os
from schemas.products import create_products_table
from helpers import get_id
from datetime import datetime

def download_img(url, folder, filename):
    response = requests.get(url)

    if response.status_code == 200:

       with open(os.path.join(folder, filename), 'wb') as file:
           file.write(response.content)

def get_content(linkProduct):
    html = requests.get(linkProduct).text
    soup = BeautifulSoup(html, 'html.parser')

    content_element = soup.select_one("#top-home")

    if content_element:
        list_content = content_element.contents

        return ''.join(map(str, list_content))

    return None

def extract_price(price_str):
    if price_str:
        price_str = price_str.replace('.', '').replace("đ", "").strip()

        return int(price_str)
    
    return None

def insert_product(cursor, mydb, items):
    sql = """ INSERT INTO products (name, link, image_link, image_name, price_current, price_old, category_id, content, source_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """
    cursor.executemany(sql, items)
    mydb.commit()

def get_products_in_category(category_url, category_id, cursor, mydb, link_main, latest_id, task):
    max_page = 100
    items_insert = []
    exit_loop = False

    for i in range(max_page):
        if exit_loop:
            break

        page_url = f"{category_url}?page={i+1}"

        html = requests.get(link_main + page_url).text
        soup = BeautifulSoup(html, 'html.parser')

        items_product = soup.select(".product-box")

        if not items_product:
            break

        for item in items_product:
            link                = item.select_one('.product-link')['href']
            source_id           = get_id(link)

            if task == 'new' and source_id <= latest_id:
                exit_loop = True
                break

            name                = item.select_one('.product-name').text
            image_link          = item.select_one('.img-fluid')['src']
            price_old_element   = item.select_one('.text-lowercase > del')
            price_old           = price_old_element.text if price_old_element else None
            price_current       = item.select_one('.text-lowercase').text
            price_current       = price_current.replace(price_old, "") if price_old_element else price_current
            price_current       = extract_price(price_current)
            price_old           = extract_price(price_old)
            
            content             = get_content(link_main + link)
            image_name          = os.path.basename(image_link)

            download_img(link_main + image_link, './images/', image_name)
            
            items_insert.append((name, link, image_link, image_name, price_current, price_old, category_id, content, source_id))    

    insert_product(cursor, mydb, items_insert)

def get_categories(cursor):
    cursor.execute("SELECT id, link FROM categories")

    return cursor.fetchall()

def get_latest_id(cursor, category_id):
    sql = """ SELECT MAX(source_id) FROM products WHERE category_id = %s """
    cursor.execute(sql, (category_id,))
    latest_id = cursor.fetchone()[0]

    return latest_id if latest_id else 0

def save_history(cursor, mydb, type, task):
    sql_insert = """ INSERT INTO history (time_get, type) VALUES (%s, %s) """
    sql_update = """ UPDATE history SET time_get = %s WHERE type = %s """

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sql = sql_insert if task == 'all' else sql_update

    cursor.execute(sql, (current_time, type))
    mydb.commit()

def main(cursor, mydb, task="all"):
    create_products_table(cursor, mydb)

    items_category = get_categories(cursor)

    link_main = 'http://demo-php-bookstore.zendvn.com/'

    for item in items_category:
        latest_id = get_latest_id(cursor, item[0])

        get_products_in_category(item[1], item[0], cursor, mydb, link_main, latest_id, task)

    save_history(cursor, mydb, "products", task)

    print(f"Get {task} products: Finish!")

