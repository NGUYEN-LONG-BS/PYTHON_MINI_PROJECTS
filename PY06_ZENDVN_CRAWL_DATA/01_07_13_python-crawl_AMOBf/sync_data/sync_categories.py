import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_all_categories(cursor):
    cursor.execute("SELECT id, link FROM categories")
    return cursor.fetchall()

def delete_category(cursor, mydb, category_id):
    sql = 'DELETE FROM categories WHERE id = %s'
    cursor.execute(sql, (category_id,))
    mydb.commit()

def update_category(cursor, mydb, category_id, category_name):
    sql = "UPDATE categories SET name = %s WHERE id = %s"
    cursor.execute(sql, (category_name, category_id))
    mydb.commit()

def update_or_delete_category(cursor, mydb, category_id, category_link, link_main):
    response        = requests.get(link_main + category_link)
    soup            = BeautifulSoup(response.text, 'html.parser')
    error_element   = soup.select_one('body > section > div > div > div > div.error-section')

    if error_element:
        delete_category(cursor, mydb, category_id)

    else:
        category_name = soup.select_one('body > div.breadcrumb-section > div > div > div > div > h2').text.strip()
        update_category(cursor, mydb, category_id, category_name)

def update_history(cursor, mydb, type):
    sql = """ UPDATE history SET time_sync = %s WHERE type = %s """

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(sql, (current_time, type))
    mydb.commit()

def main(cursor, mydb):
    link_main = 'http://demo-php-bookstore.zendvn.com'

    items_categories = get_all_categories(cursor)

    for category_id, category_link in items_categories:
        update_or_delete_category(cursor, mydb, category_id, category_link, link_main)

    update_history(cursor, mydb, "categories")
    print("Sync categories: Finish!")

    