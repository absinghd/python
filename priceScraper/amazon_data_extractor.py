#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json

# For ignoring SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter Amazon Product Url- ")

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
html = soup.prettify('utf-8')
product_json = {}

# This block of code will help extract the Brand of the item

for divs in soup.findAll('div', attrs={'class': 'a-box-group'}):
    try:
        product_json['brand'] = divs['data-brand']
        break
    except:
        pass

# This block of code will help extract the Prodcut Title of the item

for spans in soup.findAll('span', attrs={'id': 'productTitle'}):
    name_of_product = spans.text.strip()
    product_json['name'] = name_of_product
    break

# This block of code will help extract the price of the item in dollars

for divs in soup.findAll('div'):
    try:
        price = str(divs['data-asin-price'])
        product_json['price'] = '$' + price
        break
    except:
        pass
# Saving the scraped html file

with open('output_file.html', 'wb') as file:
    file.write(html)

# Saving the scraped data in json format

with open('product.json', 'w') as outfile:
    json.dump(product_json, outfile, indent=4)
print ('----------Extraction of data is complete. Check json file.----------')
