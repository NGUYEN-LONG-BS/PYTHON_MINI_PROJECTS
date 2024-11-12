import requests
from bs4 import BeautifulSoup
import os
from schemas.products import create_products_table

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

def insert_products(cursor, mydb, items):
    sql = """ INSERT INTO products (name, link, image_link, image_name, price_current, price_old, category_id, content) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
    cursor.executemany(sql, items)
    mydb.commit()

def get_products_in_category(category_url, category_id, cursor, mydb, link_main, items_insert):
    max_page = 100

    for i in range(max_page):
        page_url = f"{category_url}?page={i+1}"

        html = requests.get(link_main + page_url).text
        soup = BeautifulSoup(html, 'html.parser')

        items_product = soup.select(".product-box")

        if not items_product:
            break

        for item in items_product:
            name                = item.select_one('.product-name').text
            link                = item.select_one('.product-link')['href']
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
            
            items_insert.append((name, link, image_link, image_name, price_current, price_old, category_id, content))    


def get_categories(cursor):
    cursor.execute("SELECT id, link FROM categories")

    return cursor.fetchall()

def delete_all_products(cursor, mydb):
    sql_delete = """ DELETE FROM products """
    cursor.execute(sql_delete)

    reset_id_sql = """ ALTER TABLE products AUTO_INCREMENT = 1 """
    cursor.execute(reset_id_sql)

    mydb.commit()


def main(cursor, mydb):
    create_products_table(cursor, mydb)

    items_category = get_categories(cursor)

    link_main = 'http://demo-php-bookstore.zendvn.com/'

    items_insert = []

    for item in items_category:

        get_products_in_category(item[1], item[0], cursor, mydb, link_main, items_insert)

    delete_all_products(cursor, mydb)
    insert_products(cursor, mydb, items_insert)

    print("Get new products: Finish!")

