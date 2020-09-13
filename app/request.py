import urllib.request, json
from .models import News_source, News_article

api_key = None

base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_URL']
    
def get_news_source(sources):
    get_news_sources_url = base_url.format(sources,api_key)
    
    with urllib.request.urlopen(get_news_sources_url) as url:
        get_news_sources_data = url.read()
        get_news_sources_response = json.loads(get_news_sources_data)
        
        news_sources_result = None
        
        if get_news_sources_response['results']:
            news_source_list = get_news_sources_response['results']
            news_sources_result = process_results(news_source_list)
            
    return news_sources_result

def process_results(sources):
    news_sources_result = []
    for source_items in sources:
        id = source_items.get('id')
        name = source_items.get('name')
        description = source_items.get('description')
        category = source_items.get('category')
        language = source_items.get('language')
        
        if language == 'en':
            news_sources_object = News_source(id, name, description, category, language)
            news_sources_result.append(news_sources_object)
            
    return news_sources_result
         
    

    