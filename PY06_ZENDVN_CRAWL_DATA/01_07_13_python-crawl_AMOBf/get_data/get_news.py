import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
from datetime import datetime

from helpers import get_id

from schemas.news import create_news_table

async def extract_items(page):
    html = await page.content()
    soup = BeautifulSoup(html, 'html.parser')

    items = []

    for item in soup.select('#list-news > div'):
        name        = item.find('h4').text
        link        = item.select_one('.blog-left a')['href']
        image_link  = item.find('img')['src']
        description = item.find('p').text
        source_id   = get_id(link)

        items.append((name, link, image_link, description, source_id))

    return items

async def scrape_infinite_scroll_items(page, item_target_count, scroll_delay, latest_id, task):
    items = []                                 

    previous_height = 0

    try:
        while True:
            items = await extract_items(page)

            if len(items) >= item_target_count:
                break

            if task == 'new' and items[len(items)-1][4] <= latest_id:
                break

            previous_height = await page.evaluate('document.body.scrollHeight')
            await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            await page.waitForFunction(f'document.body.scrollHeight > {previous_height}')
            await asyncio.sleep(scroll_delay)

    except Exception as e:
        print(e)    

    return items[:item_target_count]

async def parse_news_data(html, item):
    soup            = BeautifulSoup(html, 'html.parser')
    content_element = soup.select_one('body > section > div > div > div.col-xl-9.col-lg-8.blog-detail > div.ckeditor-content') 
    list_content    = content_element.contents
    content         = ''.join(map(str, list_content))
    time_crawl      = soup.select_one('body > section > div > div > div.col-xl-9.col-lg-8.blog-detail > ul > li:nth-child(1)').text

    return sum((item, (content, time_crawl)), ())

async def crawl_page(page, link_site_get, items):
    for i in range(len(items)):
        item = items[i]
        await page.goto(link_site_get + item[1])
        html = await page.content()
        items[i] = await parse_news_data(html, item)

async def insert_news(cursor, mydb, items):
    sql = "INSERT INTO news (name, link, image_link, description, source_id, content, time_crawl) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(sql, items)
    mydb.commit()

def get_latest_id(cursor):
    sql = """ SELECT MAX(source_id) FROM news """
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

async def main(cursor, mydb, task="all"):
    create_news_table(cursor, mydb)

    link_site_get = 'http://demo-php-bookstore.zendvn.com/tin-tuc.html'

    browser = await launch(headless=False)
    page = await browser.newPage()

    await page.goto(link_site_get)

    latest_id = get_latest_id(cursor)

    items_crawl = await scrape_infinite_scroll_items(page, 21, 2, latest_id, task)

    items_crawl = [item for item in items_crawl if item[4] > latest_id]

    await crawl_page(page, link_site_get, items_crawl)

    await insert_news(cursor, mydb, items_crawl)

    save_history(cursor, mydb, "news", task)

    print(f"Get {'breaking' if task == 'new' else task } news: Finish!")

    await browser.close()