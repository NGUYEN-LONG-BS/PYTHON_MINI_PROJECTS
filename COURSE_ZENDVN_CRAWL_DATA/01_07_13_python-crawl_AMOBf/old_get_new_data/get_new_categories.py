import requests
from bs4 import BeautifulSoup

from schemas.categories import create_news_table

def insert_categories(cursor, mydb, items):
    sql = """ INSERT INTO categories (name, link) VALUES (%s, %s) """
    cursor.executemany(sql, items)
    mydb.commit()

def delete_all_categories(cursor, mydb):
    sql_delete = """ DELETE FROM categories """
    cursor.execute(sql_delete)

    reset_id_sql = """ ALTER TABLE categories AUTO_INCREMENT = 1 """
    cursor.execute(reset_id_sql)

    mydb.commit()

def main(cursor, mydb):
    url      = 'http://demo-php-bookstore.zendvn.com/index.html'
    response = requests.get(url)
    html     = response.text
    soup     = BeautifulSoup(html, 'html.parser')

    items_category = soup.select('#main-menu > li:nth-child(4) > ul > li')

    items_insert = []

    for item in items_category:
        name = item.select_one('a').text
        link = item.select_one('a')['href']

        items_insert.append((name, link))

    delete_all_categories(cursor, mydb)
    insert_categories(cursor, mydb, items_insert)

    print("Get new categories: Finish!")