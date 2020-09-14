from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_article
from ..models import News_source

@main.route('/')
def index():
    general_news = get_sources('general')
    sports_news = get_sources('sports')
    technology_news = get_sources('technology')
    entertainment_news = get_sources('entertainment')
    business_news = get_sources('business')
    science_news = get_sources('science')
    return render_template('index.html', general=general_news,sports=sports_news,technology=technology_news,entertainment=entertainment_news,business=business_news,science=science_news)

@main.route('/articles')
def news_articles():
    cnn = get_article('cnn')
    argaam_news = get_article('argaam')
    return render_template('articles.html',cnn=cnn,argaam=argaam_news)