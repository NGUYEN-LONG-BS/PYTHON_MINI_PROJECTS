import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def get_order_login():
    link_site_login = 'http://demo-php-bookstore.zendvn.com/dang-nhap.html'
    link_site_get   = 'http://demo-php-bookstore.zendvn.com/lich-su-mua-hang.html'

    browser = await launch(headless=False)
    page = await browser.newPage()

    await page.goto(link_site_login)
    await page.type('input[type=email]', 'admin@gmail.com')
    await page.type('input[type=password]', '12345678')
    await page.click('button#submit')
    await asyncio.sleep(3)
    await page.goto(link_site_get)

    html = await page.content()

    await browser.close()

    return html

async def parse_order_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    items_order = soup.select('.card')
    items_crawl = []

    for item in items_order:
        order_code = item.find('button').get_text()
        created = item.find('h5').get_text().replace(order_code, "").replace("Thời gian:", "").strip()

        order_code = order_code.replace("Mã đơn hàng:", "").strip()

        items_crawl.append((order_code, created))

    print(items_crawl)

async def main():
    html = await get_order_login()
    await parse_order_data(html)

asyncio.run(main())    
