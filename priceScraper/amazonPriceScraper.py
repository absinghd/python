import asyncio
from pyppeteer import launch
import json
import schedule
import time
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC4320ae6e316a32e5ed020e04624ec852"
# Your Auth Token from twilio.com/console
auth_token  = "c4df930c37ff7f23ed3f605ba6c82dea"

client = Client(account_sid, auth_token)

#message = client.messages.create(
    #to="+15594927278", 
    #from_="+12015968412",
    #body="Price is same!")

#print(message.sid)



def job():
    #url = input("which link? ")
    url = "https://www.amazon.com/Graco-SlimFit-Convertible-Seat-Annabelle/dp/B01MTM3IVQ/"
    urlName = url.split('/')
    productName = urlName[3]

    with open('data.txt') as json_file:
        data = json.load(json_file)
        for p in data['product']:
            name = 'name'
            cost = p['price']
            print('Name: ' + p['name'])
            print('Price: ' + p['price'])
            print('')


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
            
            #print(productName)
            #print(price)

            if cost == price:
                print('price is same')
                message = client.messages.create(
                    to="+15594927278", 
                    from_="+12015968412",
                    body="Price is same!")

            data['product'] = []
            data['product'].append({
                'name': productName,
                'price': price,
                })

            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)

            print(data)


        except:
            print('Error')






    asyncio.get_event_loop().run_until_complete(main())

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)