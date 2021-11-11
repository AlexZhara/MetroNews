"""Database model, based on the flask_sqlalchemy package"""

from api import db

class NewsPost(db.Model):
	__tablename__ = 'news_posts'

	id = db.Column(db.Integer, primary_key=True)
	headline = db.Column(db.String, nullable=False)
	img_url = db.Column(db.String, nullable=False)
	time_posted = db.Column(db.DateTime, nullable=False)
	time_parsed = db.Column(db.DateTime, nullable=False)

	def __repr__(self):
		return 'NewsPost(id={}, headline={}, img_url={}, time_posted={}, time_parsed={})'\
			.format(self.id, self.headline, self.img_url, self.time_posted, self.time_parsed)

	@property
	def serialize(self):
		"""For convenient jsonify"""
		return {
			'id' : self.id,
			'headline' : self.headline,
			'img_url' : self.img_url,
			'time_posted' : self.time_posted.__str__(),
			'time_parsed' : self.time_parsed.__str__()
		}