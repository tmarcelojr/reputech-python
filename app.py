import requests as req
from bs4 import BeautifulSoup as soup 

# Need headers due to websites preventing non-browseer user agents strings such as our Python path sent by our Python library. By setting our headers we are telling the browser the user agent is a common client
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

#
page_html = req.get('https://www.glassdoor.com/Overview/Working-at-Braintree-EI_IE424728.11,20.htm', headers=headers)

# This gives us a class of request
print(type(page_html))

# This will change our request into a BeautifulSoup so we can scrape
soup = soup(page_html.text, 'html.parser')

# Grab the Company Name 
print(soup.find('span', id='DivisionsDropdownComponent').getText()) # Returns Braintree

# Finds all the number of reviews
reviews = soup.find_all('span', class_="num h2")
reviews_results = []
for each_reviews in reviews:
	reviews_results.append(each_reviews)

# Number of Company Reviews
print('\nThis is the number of company reviews.')
print(reviews_results[1].getText())

# Number of Salary Reviews
print('\nThis is the number of salary reviews.')
print(reviews_results[3].getText())

# Number of Interview Reviews
print('\nThis is the number of interview reviews.')
print(reviews_results[4].getText())

# Number of Benefits Reviews
print('\nThis is the number of benefits reviews.')
print(reviews_results[5].getText())





