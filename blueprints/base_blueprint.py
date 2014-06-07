from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

page = Blueprint('base_page', __name__, template_folder='templates')

@page.route('/', defaults={'page': 'index'})
@page.route('/<page>')
def show(page):
    try:
        return render_template('base/%s.html' % page)
    except TemplateNotFound:
        abort(404)
