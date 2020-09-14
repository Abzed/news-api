import urllib.request, json
from .models import News_source, News_article

api_key = None

base_url = None

article_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_URL']
    
def get_sources(category):
    get_sources_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        sources_result = None
        
        if get_sources_response['sources']:
            sources_result_list = get_sources_response['sources']
            sources_result = process_results(sources_result_list)
    return sources_result

def process_results(sources_list):
    sources_result = []
    for sources_items in sources_list:
        id = sources_items.get('id')
        name = sources_items.get('name')
        description = sources_items.get('description')
        category = sources_items.get('category')
        url = sources_items.get('url')
        
        if description:
            sources_object = News_source(id, name, description, category, url)
            sources_result.append(sources_object)
            
    return sources_result

def get_article(sources):
    get_article_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(sources,api_key)
    
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)
        
        article_results = None
        
        if get_article_response['articles']:
            article_result_list = get_article_response['articles']
            article_results = process_articles(article_result_list)
            
    return article_results

def process_articles(article_list):
    article_results = []
    for article_items in article_list:
        source_name = article_items.get('source.name')
        author = article_items.get('author')
        title = article_items.get('title')
        description = article_items.get('description')
        url_link = article_items.get('url')
        url_image = article_items.get('urlToImage')
        date_published = article_items.get('publishedAt')
        content = article_items.get('content')
        
        if url_image:
            article_object = News_article(source_name, author, title, description,url_link, url_image,date_published, content)
            article_results.append(article_object)
        
    return article_results
        
        
    