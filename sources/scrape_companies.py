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

company_names = []
company_websites = []
company_website_logos = []

def get_text():
	for data in websites_data:
		page_html = soup(data.text, 'html.parser')
		logos = page_html.find_all('span', class_='sqLogo tighten medSqLogo logoOverlay')
		websites = page_html.find_all('span', class_='value website')
		names = page_html.find_all('span', id='DivisionsDropdownComponent')

		# WEBSITE LINKS
		for website in websites:
			web_links = website.find_all('a')
			for web_link in web_links:
				link = web_link.getText()
				company_websites.append(link)

		# WEBSITE LOGOS
		for logo in logos:
			logo_data = logo.find_all('img')
			img_src = logo_data[0].get('src')
			company_website_logos.append(img_src)

		# WEBSITE NAME
		for name in names:
			website_name = name.getText()
			company_names.append(website_name)


# Only call when needed.
# asyncio.run(main())
# get_text()



