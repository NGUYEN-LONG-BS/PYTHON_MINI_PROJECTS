import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_all_products(cursor):
    cursor.execute("SELECT id, link FROM products")
    return cursor.fetchall()

def delete_product(cursor, mydb, product_id):
    sql = 'DELETE FROM products WHERE id = %s'
    cursor.execute(sql, (product_id,))
    mydb.commit()

def update_product(cursor, mydb, product_id, name, content):
    sql = "UPDATE products SET name = %s, content = %s WHERE id = %s"
    cursor.execute(sql, (name, content, product_id))
    mydb.commit()

def update_or_delete_product(cursor, mydb, product_id, product_link, link_main):
    response        = requests.get(link_main + product_link)
    soup            = BeautifulSoup(response.text, 'html.parser')
    error_element   = soup.select_one('body > section > div > div > div > div.error-section')

    if error_element:
        delete_product(cursor, mydb, product_id)

    else:
        name            = soup.select_one('body > section > div > div > div:nth-child(1) > div.col-lg-9.col-sm-12.col-xs-12 > div > div:nth-child(2) > div.col-lg-8.col-xl-8.rtl-text > div > h2').text.strip()
        content_element = soup.select_one('#top-home')
        list_content    = content_element.contents
        content         = ''.join(map(str, list_content))

        update_product(cursor, mydb, product_id, name, content)

def update_history(cursor, mydb, type):
    sql = """ UPDATE history SET time_sync = %s WHERE type = %s """

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(sql, (current_time, type))
    mydb.commit()

def main(cursor, mydb):
    link_main = 'http://demo-php-bookstore.zendvn.com'

    items_product = get_all_products(cursor)

    for product_id, product_link in items_product:
        update_or_delete_product(cursor, mydb, product_id, product_link, link_main)

    update_history(cursor, mydb, "products")
    print("Sync products: Finish!")

    