from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news_source
from ..models import News_source

@main.route('/')
def index():
    return render_template('index.html')