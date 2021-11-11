"""Основной модуль парсера.

Создает базу данных при первом запуске, и заполняет новостями, потом запускает schedule процесс.

При наличии файла app.db в корневой папке, сразу запускает schedule процесс.

"""

import os
import schedule
import time
from datetime import datetime
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from parser import Parser
from models import NewsPost

SCHEDULER_CONFIG = 5 # Как часто парсится страница, в минутах

"""
def test_task():
	print('Current timestamp is {}'.format(datetime.now().timestamp()))
"""

def get_db_filepath():
	current_dir = os.path.abspath(os.path.dirname(__file__))
	main_dir = os.path.dirname(current_dir)
	return main_dir + '/app.db'

def create_database():
	print('The database does not exist. Creating the database...')
	db_filepath = get_db_filepath()
	engine = create_engine('sqlite:///' + db_filepath, echo=False)
	NewsPost.metadata.create_all(engine)
	print('Table news_posts successfully created in ' + db_filepath)

	page = parser.get_page()
	all_posts = parser.parse_front_page_full(page)
	print('News page successfully parsed.')
	
	with Session(engine) as session:
		for post in reversed(all_posts): # reversed чтобы id инкрементировались в правильном порядке
			row = NewsPost(**post)
			session.add(row)
		session.commit()
	print('Rows successfully inserted.')

def scheduled_parse():
	print('Current time is {}'.format(str(datetime.now())))
	page = parser.get_page()
	all_posts = parser.parse_front_page_full(page)

	for i in range(len(all_posts)):
		latest_post_time = parser.get_post_time(all_posts[i])
		print('Recent news was posted @ {}'.format(latest_post_time))
		print('Checking if a post with this time exists in the database...')

		engine = create_engine('sqlite:///' + get_db_filepath())

		with Session(engine) as session:
			count = session.query(NewsPost).filter(NewsPost.time_posted == latest_post_time).count()

		if count == 1:
			print('This post already exists in the database. Will check again in {} minutes.'.format(SCHEDULER_CONFIG))
			break
		else:
			print('New post detected! Capturing into the database...')
			latest_post = all_posts[i]
			with Session(engine) as session:
				row = NewsPost(**latest_post)
				session.add(row)
				session.commit()
			print('Successfully saved the post. Checking if the next post already exists...')

if __name__ == '__main__':
	parser = Parser()

	db_filepath = get_db_filepath()

	if not os.path.isfile(db_filepath):
		create_database()

	print('The database exists! Launching parser, scheduled for every {} minutes...'.format(str(SCHEDULER_CONFIG)))
	schedule.every(SCHEDULER_CONFIG).minutes.do(scheduled_parse)

	while True:
		schedule.run_pending()
		time.sleep(1)




	
	