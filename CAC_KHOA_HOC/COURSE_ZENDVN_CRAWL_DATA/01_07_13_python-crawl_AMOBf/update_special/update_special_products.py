import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
from helpers import get_id

async def get_product_ajax():
    link_site_get = 'http://demo-php-bookstore.zendvn.com/index.html'

    browser = await launch(headless=False)
    page = await browser.newPage()

    await page.goto(link_site_get)
    await page.click('body > section:nth-child(8) > div > div > div > div > ul > li:nth-child(2) > a')
    await asyncio.sleep(3)
    await page.click('body > section:nth-child(8) > div > div > div > div > ul > li:nth-child(3) > a')
    await asyncio.sleep(3)

    html = await page.evaluate("() => document.querySelector('html').outerHTML")
    
    await browser.close()

    return html

async def update_special_in_db(cursor, mydb, source_id):
    sql = "UPDATE products SET special = true WHERE source_id = %s"
    cursor.execute(sql, (source_id,))
    mydb.commit()

async def parse_product_data(cursor, mydb, html):
    soup = BeautifulSoup(html, 'html.parser')
    items_product = soup.select('.product-box')

    for item in items_product:
        link      = item.select_one('.product-link')['href']
        source_id = get_id(link)

        await update_special_in_db(cursor, mydb, source_id)

async def main(cursor, mydb):
    html = await get_product_ajax()
    await parse_product_data(cursor, mydb, html)

    print("Update special products: Finish!")

