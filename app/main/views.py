from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources
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
    health_news = get_sources('health')
    return render_template('articles.html', health=health_news)