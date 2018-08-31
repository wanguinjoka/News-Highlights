from app import app
import urllib.request,json
from .models import source

Source = source.Source

# getting the api key
apiKey = app.config['SOURCE_API_KEY']

#getting the source base urlli
base_url = app.config['SOURCE_API_BASE_URL']

def get_source(category):
    '''
    function that gets the json url request
    '''
    get_source_url = base_url.format(category,apiKey )

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        # print(get_source_response)
        source_sources = None

        if get_source_response['sources']:
            source_sources_list = get_source_response['sources']
            source_sources = process_sources(source_sources_list)

    return source_sources

def process_sources(source_list):
    '''
    Function that process the source articles and transform them to a list of objects

    args:
        source_list ia a dictionaries that contain source get_source_data
    returns:
        source_articles: is alist of source objects
    '''
    source_sources = []
    for source_item in source_list:
        id=source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')

        if id:
            source_object = Source(id,name,description,url,category,country)
            source_sources.append(source_object)

    return source_sources
