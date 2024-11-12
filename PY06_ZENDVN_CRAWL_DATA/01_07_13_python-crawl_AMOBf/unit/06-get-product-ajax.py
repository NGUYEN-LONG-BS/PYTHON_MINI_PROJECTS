import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

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

async def parse_product_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items_product = soup.select('.tab-content-cls .product-box')

    items_crawl = []

    for item in items_product:
        name                = item.select_one('.product-name').text
        link                = item.select_one('.product-link')['href']
        image_link          = item.select_one('.img-fluid')['src']
        price_old_element   = item.select_one('.text-lowercase > del')
        price_old           = price_old_element.text if price_old_element else None
        price_current       = item.select_one('.text-lowercase').text
        price_current       = price_current.replace(price_old, "") if price_old_element else price_current

        items_crawl.append((name, link, image_link, price_old, price_current))

    print(items_crawl)


async def main():
    html = await get_product_ajax()
    await parse_product_data(html)

asyncio.run(main())