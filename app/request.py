import urllib.request, json
from .models import News_source, News_article

api_key = None

base_url = None

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
        language = sources_items.get('language')
        
        if description:
            sources_object = News_source(id, name, description, category, language)
            sources_result.append(sources_object)
            
    return sources_result
        
    