# Database models

from datetime import datetime
from api import db

class NewsPost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	header = db.Column(db.String, nullable=False)
	img_url = db.Column(db.String, nullable=False)
	time_posted = db.Column(db.DateTime, nullable=False)
	time_parsed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return 'NewsPost({}, {}, {})'.format(self.header, self.img_url, self.time_posted)