import asyncio
from pyppeteer import launch

url = input("which link? ")

urlName = url.split('/')
productName = urlName[3]

async def main():
    try:
        browser = await launch()
        page = await browser.newPage()
        await page.goto(url)
  #  await page.screenshot({'path': 'example.png'})
        await page.waitForSelector("#priceblock_ourprice")
        element = await page.querySelector('#priceblock_ourprice')
        price = await page.evaluate('(element) => element.textContent', element)
        #element2 = await page.querySelector("#productTitle")
        #title = await page.evaluate('(element) => element.textContent', element2)

    
    # print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
        await browser.close()
        #print(title)
        print(productName)
        print(price)

    except:
        print('Error')

asyncio.get_event_loop().run_until_complete(main())