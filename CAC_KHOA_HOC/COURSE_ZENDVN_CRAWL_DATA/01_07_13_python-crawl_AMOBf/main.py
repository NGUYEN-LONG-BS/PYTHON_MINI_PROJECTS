import mysql.connector
import asyncio
import schedule
import time

from get_data import get_categories, get_products, get_news
from sync_data import sync_categories, sync_products, sync_news
from update_special import update_special_categories, update_special_news, update_special_products
# from get_new_data import get_new_categories, get_new_products, get_breaking_news

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        # password="password",
        database="python_crawl"
    )
cursor = mydb.cursor()

def get_all_data():
    get_categories.main(cursor, mydb)
    get_products.main(cursor, mydb)
    asyncio.run(get_news.main(cursor, mydb))

def get_new_data():
    get_categories.main(cursor, mydb, 'new')
    get_products.main(cursor, mydb, 'new')
    asyncio.run(get_news.main(cursor, mydb, 'new'))

def sync_data():
    sync_categories.main(cursor, mydb)
    sync_products.main(cursor, mydb)
    sync_news.main(cursor, mydb)

def update_special():
    update_special_categories.main(cursor, mydb)
    update_special_news.main(cursor, mydb)
    asyncio.run(update_special_products.main(cursor, mydb))

def main():
    # get_all_data()
    get_new_data()
    sync_data()
    update_special()
    cursor.close()
    mydb.close()

schedule.every(5).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
