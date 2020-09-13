import urllib.request, json
from .models import News_source, News_article

api_key = None

base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_URL']
    
def get_news_source(category):
    get_news_source_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)
        
        news_sources_result = None
        
        if get_news_source_response['sources']:
            news_source_list = get_news_source_response['sources']
            news_source_result = process_results(news_source_list)
            
    return news_sources_result

def process_results(sources_list):
    news_source_result = []
    for source_items in sources_list:
        id = source_items.get('id')
        name = source_items.get('name')
        description = source_items.get('description')
        category = source_items.get('category')
        language = source_items.get('language')
        
        if language == 'en':
            news_source_object = News_source(id, name, description, category, language)
            news_source_result.append(news_source_object)
            
    return news_source_result
         
    

    