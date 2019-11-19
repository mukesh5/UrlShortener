from flask import Flask
import flask_whooshalchemy as whooshlchemy

from .models import Link
from .extensions import db
from .routes import short

def create_app(config_file='settings.py'):
	app = Flask(__name__)

	app.config.from_pyfile(config_file)
	
	db.init_app(app)

	app.register_blueprint(short)

	whooshlchemy.whoosh_index(app, Link)

	return app