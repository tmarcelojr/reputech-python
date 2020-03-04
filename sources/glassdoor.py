import requests as req
import asyncio
from bs4 import BeautifulSoup as soup
from sources.glassdoor_company_links import *

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

def get_link(link):
	return req.get(link, headers=headers);

# aysncio to wait for res for each link called in main()
async def get_responses(link):
	coroutine_version = asyncio.coroutine(get_link)
	return await coroutine_version(link)

websites_data = []
async def main():
	for link in glassdoor_company_links:
		websites_data.append(await asyncio.create_task(get_responses(link)))

glassdoor_company_ratings = []
glassdoor_benefits_ratings = []
glassdoor_salary_ratings = []
glassdoor_interview_ratings = []
glassdoor_rating = []

def get_text():
	for data in websites_data:
		soup_data = soup(data.text, 'html.parser')
		reviews = soup_data.find_all('span', class_='num h2')
		rating = soup_data.find(class_='hidden rating').getText()
		glassdoor_rating.append(rating)
		for idx, review in enumerate(reviews):
			review_data = review.getText()
			if idx != 0 and idx != 2 and review_data != '--':
				if 'k' in review_data:
					num_data = float(review_data.replace('k', '')) * 1000
					if idx == 1: glassdoor_company_ratings.append(int(num_data))
					elif idx == 3: glassdoor_salary_ratings.append(int(num_data))
					elif idx == 4: glassdoor_interview_ratings.append(int(num_data))
					elif idx == 5: glassdoor_benefits_ratings.append(int(num_data))
				else:
					num_data = float(review_data)
					if idx == 1: glassdoor_company_ratings.append(int(num_data))
					elif idx == 3: glassdoor_salary_ratings.append(int(num_data))
					elif idx == 4: glassdoor_interview_ratings.append(int(num_data))
					elif idx == 5: glassdoor_benefits_ratings.append(int(num_data))


# Only call when needed.
# asyncio.run(main())
# get_text()



