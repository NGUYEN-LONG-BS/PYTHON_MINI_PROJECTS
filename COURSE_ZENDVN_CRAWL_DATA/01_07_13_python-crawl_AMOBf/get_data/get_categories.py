import requests
from bs4 import BeautifulSoup
from helpers import get_id
from datetime import datetime

from schemas.categories import create_news_table
from schemas.history import create_history_table

def insert_categories(cursor, mydb, items):
    sql = """ INSERT INTO categories (name, link, source_id) VALUES (%s, %s, %s) """
    cursor.executemany(sql, items)
    mydb.commit()

def get_latest_id(cursor):
    sql = """ SELECT MAX(source_id) FROM categories """
    cursor.execute(sql)
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
    url      = 'http://demo-php-bookstore.zendvn.com/index.html'
    response = requests.get(url)
    html     = response.text
    soup     = BeautifulSoup(html, 'html.parser')

    items_category = soup.select('#main-menu > li:nth-child(4) > ul > li')

    items_insert = []

    latest_id = get_latest_id(cursor) if task == 'new' else 0

    for item in items_category:
        name        = item.select_one('a').text
        link        = item.select_one('a')['href']
        source_id   = get_id(link)

        if task == 'new' and source_id <= latest_id:
            continue

        items_insert.append((name, link, source_id))

    create_news_table(cursor, mydb)
    insert_categories(cursor, mydb, items_insert)

    create_history_table(cursor, mydb)
    save_history(cursor, mydb, "categories", task)

    print(f"Get {task} categories: Finish!")