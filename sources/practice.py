import requests as req
import asyncio
from bs4 import BeautifulSoup as soup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

page_html = req.get('https://www.indeed.com/cmp/Capital-One', headers=headers)
soup = soup(page_html.text, 'html.parser')


reviews = soup.find_all('li', class_='cmp-CompactHeaderMenuItem')
item = reviews[2].find('div', class_='cmp-CompactHeaderMenuItem-count')

print(item.getText())
# for review in reviews:
# 	converted = review.getText()
# 	print(converted)