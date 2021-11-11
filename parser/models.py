#models.py

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class NewsPost(Base):
	__tablename__ = 'news_posts'

	id = Column('id', Integer, primary_key=True)
	headline = Column('headline', String, nullable=False)
	img_url = Column('img_url', String, nullable=False)
	time_posted = Column('time_posted', DateTime, nullable=False)
	time_parsed = Column('time_parsed', DateTime, nullable=False)

	def __repr__(self):
		return 'NewsPost(id={}, headline={}, img_url={}, time_posted={}, time_parsed={})'\
			.format(self.id, self.headline, self.img_url, self.time_posted, self.time_parsed)