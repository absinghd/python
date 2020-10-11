from urllib.request import urlopen
url = input('what product price do you want to track? ')

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)