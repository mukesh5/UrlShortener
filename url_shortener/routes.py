from flask import Blueprint, render_template, request, redirect

from .extensions import db
from .models import Link

short = Blueprint('short', __name__)

@short.route('/search', methods=['POST'])
def search():
	pattern = request.form['pattern']
	urls = Link.query.whoosh_search(pattern).all()
	return render_template('stats.html', urls=urls)


@short.route('/<short_url>')
def redirect_to_url(short_url):
	link = Link.query.filter_by(short_url=short_url).first_or_404()

	link.visits = link.visits + 1
	db.session.commit()
	return redirect(link.original_url)



@short.route('/')
def index():
	return render_template('index.html')



@short.route('/add_link', methods=['POST'])
def add_link():
	original_url = request.form['original_url']
	url = Link(original_url=original_url)
	db.session.add(url)
	db.session.commit()

	return render_template('link_added.html', 
		new_url=url.short_url, original_url=url.original_url)



@short.route('/stats')
def stats():
	urls = Link.query.all()

	return render_template('stats.html', urls = urls)


@short.errorhandler(404)
def page_not_found(e):
	return '<h1>404 Not Found</h1>', 404

