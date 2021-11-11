# Routes

from flask import request

from app import app

@app.route('/')
def hello_world():
	return('Hello, world!')

@app.route('/metro/news', methods=['GET'])
def metro_news():
	if request.args.get != None:
		date_range = request.args.get('day')
		return 'Entries from the date range of {}'.format(date_range)
	else:
		return 'All the entries'