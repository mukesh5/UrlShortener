from datetime import datetime
from random import choices
import string


from .extensions import db


class Link(db.Model):
	__searchable__ = ['original_url']

	id = db.Column(db.Integer, primary_key=True)
	original_url = db.Column(db.String(512))
	short_url = db.Column(db.String(5), unique=True)
	visits = db.Column(db.Integer, default=0)
	date_created = db.Column(db.DateTime, default = datetime.now)

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.short_url = self.generate_short_url()



	def generate_short_url(self):
		characters = string.digits + string.ascii_letters
		short_url = ''.join(choices(characters, k=5))

		url = self.query.filter_by(short_url=short_url).first()

		if url:
			return generate_short_url()
		else:
			return short_url

