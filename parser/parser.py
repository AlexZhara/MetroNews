# Metro news parser

import schedule
import time
import requests
import re
from bs4 import BeautifulSoup


class Parser:
	url = 'https://mosmetro.ru/news/'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	all_posts = soup.find_all('a', class_='news-card')
	for post in all_posts:
		if len(post['class']) > 1 and post['class'][1] == 'hidden':
			continue
		#print(post.prettify())

		header = post.find('div', class_='news-card__caption').get_text()

		img = post.find('div', class_='news-card__image')
		img_url = re.search('\(([^)]+)', img['style']).group(1)

		time_str = post.find('div', class_='news-card__date').get_text()
		print(time_str)
		


parser = Parser()