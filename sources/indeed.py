import requests as req
import asyncio
from bs4 import BeautifulSoup as soup
from sources.indeed_company_links import *

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

def get_link(link):
	return req.get(link, headers=headers);

# aysncio to wait for res for each link called in main()
async def get_responses(link):
	coroutine_version = asyncio.coroutine(get_link)
	return await coroutine_version(link)

websites_data = []
async def main():
	for link in indeed_company_links:
		websites_data.append(await asyncio.create_task(get_responses(link)))

company_ratings = []
benefits_ratings = []
salary_ratings = []
interview_ratings = []

def get_text():
	for data in websites_data:
		soup_data = soup(data.text, 'html.parser')
		reviews = soup_data.find_all('a', class_='cmp-CompactHeaderMenuItem-link cmp-u-noUnderline')
		for idx, review in enumerate(reviews):
			review_data = review.find('div', class_='cmp-CompactHeaderMenuItem-count')
			if review_data != None:
				review_data_text = review_data.getText()
				if idx != 0 and idx != 1 and idx != 5 and idx != 6:
					if 'K' in review_data_text:
						# float takes in int and strings and returns floating int
						# float removes white spaces and '.', i.e., '7.7k'
						# int the floating int for better ui in client
						num_data = float(review_data_text.replace('K', '')) * 1000
						if idx == 2: company_ratings.append(int(num_data))
						elif idx == 3: salary_ratings.append(int(num_data))
						elif idx == 4: benefits_ratings.append(int(num_data))
						elif idx == 7: interview_ratings.append(int(num_data))
					else:
						if idx == 2: company_ratings.append(int(review_data_text))
						elif idx == 3: salary_ratings.append(int(review_data_text))
						elif idx == 4: benefits_ratings.append(int(review_data_text))
						elif idx == 7: interview_ratings.append(int(review_data_text))
			else:
				num_data = 0
				if idx == 2: company_ratings.append(num_data)
				elif idx == 3: salary_ratings.append(num_data)
				elif idx == 4: benefits_ratings.append(num_data)
				elif idx == 7: interview_ratings.append(num_data)

# Only call when needed.
asyncio.run(main())
get_text()



