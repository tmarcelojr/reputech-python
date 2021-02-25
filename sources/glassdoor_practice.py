	import requests as req
import asyncio
from bs4 import BeautifulSoup as soup
from glassdoor_company_links import *
from glassdoor_interview_links import *
from glassdoor_benefits_links import *

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

def get_link(link):
	return req.get(link, headers=headers);

# aysncio to wait for res for each link called in main()
async def get_responses(link):
	coroutine_version = asyncio.coroutine(get_link)
	return await coroutine_version(link)

websites_data = []
websites_interview_data = []
websites_benefits_data = []

websites_r
async def main():
	for link in glassdoor_company_links:
		websites_data.append(await asyncio.create_task(get_responses(link)))

	for interview_link in glassdoor_interview_links:
		websites_interview_data.append(await asyncio.create_task(get_responses(interview_link)))

	for benefits_link in glassdoor_benefits_links:
		websites_benefits_data.append(await asyncio.create_task(get_responses(benefits_link)))


def get_text():
	for data in websites_data:
		soup_data = soup(data.text, 'html.parser')
		rating = soup_data.find(class_='hidden rating').getText()
		print('this is our overall glassdoor rating', rating)

	# for data in websites_interview_data:
	# 	soup_data = soup(data.text, 'html.parser')
	# 	rating = soup_data.find(class_='difficultyLabel subtle').getText()
	# 	print('this is the difficulty level', rating)

	# for data in websites_benefits_data:
	# 	soup_data = soup(data.text, 'html.parser')
	# 	rating = soup_data.find(class_='ratingNum rating').getText()
	# 	print('this is the average benefits rating', rating)


# Only call when needed.
# asyncio.run(main())
# get_text()



