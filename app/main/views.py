from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources
from ..models import News_source

@main.route('/')
def index():
    general_news = get_sources('general')
    return render_template('index.html', general=general_news)