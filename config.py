# Config object

import os

basedir = os.path.abspath(os.path.dirname(__file__))

print('BASE DIRECTORY IS' + basedir)

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'placeholder_key'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')