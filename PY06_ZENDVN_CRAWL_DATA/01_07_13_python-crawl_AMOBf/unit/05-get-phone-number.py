import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('http://demo-php-bookstore.zendvn.com/index.html')
    await page.click('#btn-get-phone-number')
    await asyncio.sleep(3)
    phone_number = await page.evaluate("() => document.querySelector('#btn-get-phone-number').textContent")
    await browser.close()

    print(phone_number)

asyncio.run(main())