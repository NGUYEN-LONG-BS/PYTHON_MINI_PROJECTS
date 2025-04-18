import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
import mysql.connector
from schemas.news import create_news_table

async def extract_items(page):
    html = await page.content()
    soup = BeautifulSoup(html, 'html.parser')

    items = []

    for item in soup.select('#list-news > div'):
        name = item.find('h4').text
        link = item.select_one('.blog-left a')['href']
        image_link = item.find('img')['src']
        description = item.find('p').text

        items.append((name, link, image_link, description))

    return items

async def scrape_infinite_scroll_items(page, item_target_count, scroll_delay=2):
    items = []                                 

    previous_height = 0

    try:
        while True:
            items = await extract_items(page)

            if len(items) >= item_target_count:
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
    sql = "INSERT INTO news (name, link, image_link, description, content, time_crawl) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.executemany(sql, items)
    mydb.commit()

def delete_all_news(cursor, mydb):
    sql_delete = """ DELETE FROM news """
    cursor.execute(sql_delete)

    reset_id_sql = """ ALTER TABLE news AUTO_INCREMENT = 1 """
    cursor.execute(reset_id_sql)

    mydb.commit()

async def main(cursor, mydb):
    create_news_table(cursor, mydb)

    link_site_get = 'http://demo-php-bookstore.zendvn.com/tin-tuc.html'

    browser = await launch(headless=False)
    page = await browser.newPage()

    await page.goto(link_site_get)

    items_crawl = await scrape_infinite_scroll_items(page, 21)

    await crawl_page(page, link_site_get, items_crawl)

    delete_all_news(cursor, mydb)

    await insert_news(cursor, mydb, items_crawl)

    print("Get breaking news: Finish!")

    await browser.close()