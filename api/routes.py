# Routes

from flask import request, jsonify
from datetime import datetime, timedelta

from api import app
from api.models import NewsPost

@app.route('/')
def hello_world():
	return('Hello, world!')

@app.route('/metro/news', methods=['GET'])
def metro_news():
	date_range = request.args.get('day')

	if date_range is None:
		news_posts = NewsPost.query.order_by(NewsPost.time_posted).all()
		return jsonify(data=[i.serialize for i in news_posts])
	else:
		today = datetime.now()
		past_date = str(today - timedelta(days=int(date_range)))
		news_posts = NewsPost.query.filter(NewsPost.time_posted >= past_date).order_by(NewsPost.time_posted)
		return jsonify(data=[i.serialize for i in news_posts])