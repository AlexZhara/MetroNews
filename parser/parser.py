# Metro news parser

import locale
import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup
from pprint import pprint

locale.setlocale(locale.LC_ALL, 'ru_RU')

def replace_xa0(string):
	return string.replace(u'\xa0', u' ')

class Parser:
	URL = 'https://mosmetro.ru/news/'
	
	def get_page(self):
		try:
			page = requests.get(self.URL)
			return page
		except requests.exceptions.HTTPError as errh:
			print ('HTTP Error: ', errh)
			return 'Will try again in 10 minutes...'
		except requests.exceptions.ConnectionError as errc:
			print ('Connection Error: ', errc)
			return 'Will try again in 10 minutes...'
		except requests.exceptions.Timeout as errt:
			print ('Timeout Error:', errt)
			return 'Will try again in 10 minutes...'
		except requests.exceptions.RequestException as err:
			print ('Request Exception: ', err)
			return 'Will try again in 10 minutes...'
		self.page = page

	@staticmethod
	def parse_front_page_full(page):
		soup = BeautifulSoup(page.content, 'html.parser')
		find_posts = soup.find_all('a', class_='news-card')

		all_posts = []

		for post in find_posts:
			if len(post['class']) > 1 and post['class'][1] == 'hidden':
				continue

			utc_timestamp = datetime.utcnow().timestamp()

			headline = post.find('div', class_='news-card__caption').get_text().replace(u'\xa0', u' ')
			headline = replace_xa0(headline)

			img = post.find('div', class_='news-card__image')
			img_url = re.search('\(([^)]+)', img['style']).group(1)

			time_str = post.find('div', class_='news-card__date').get_text()
			date = datetime.strptime(time_str, '%d %B, %H:%M').replace(year=datetime.now().year)

			news_post = {
				'headline' : headline,
				'img_url' : img_url,
				'time_posted' : date,
				'time_parsed' : datetime.fromtimestamp(utc_timestamp)
			}

			all_posts.append(news_post)

		return all_posts

	@staticmethod
	def parse_front_page_latest(page):
		soup = BeautifulSoup(page.content, 'html.parser')
		post = soup.find('a', class_='news-card')

		utc_timestamp = datetime.utcnow().timestamp()

		headline = post.find('div', class_='news-card__caption').get_text().replace(u'\xa0', u' ')
		headline = replace_xa0(headline)

		img = post.find('div', class_='news-card__image')
		img_url = re.search('\(([^)]+)', img['style']).group(1)

		time_str = post.find('div', class_='news-card__date').get_text()
		date = datetime.strptime(time_str, '%d %B, %H:%M').replace(year=datetime.now().year)

		news_post = {
			'headline' : headline,
			'img_url' : img_url,
			'time_posted' : date,
			'time_parsed' : datetime.fromtimestamp(utc_timestamp)
		}

		return news_post

	@staticmethod
	def get_post_time(post):
		return post['time_posted']




