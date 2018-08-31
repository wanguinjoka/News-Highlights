from app import app
import urllib.request,json
from .models import source

Source = source.Source

# getting the api key
apiKey = app.config['SOURCE_API_KEY']

#getting the source base urlli
base_url = app.config['SOURCE_API_BASE_URL']

def get_source(id):
    '''
    function that gets the json url request
    '''
    get_source_url = base_url.format(id, apiKey)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        print(get_source_response)
        source_articles = None

        if get_source_response['articles']:
            source_articles_list = get_source_response['articles']
            source_articles = process_articles(source_articles_list)

    return source_articles

def process_articles(source_list):
    '''
    Function that process the source articles and transform them to a list of objects

    args:
        source_list ia a dictionaries that contain source get_source_data
    returns:
        source_articles: is alist of source objects
    '''
    source_articles = []
    for source_item in source_list:
        id=source_item.get('id')
        name = source_item.get('name')
        title = source_item.get('title')
        description = source_item.get('description')
        url = source_item.get('url')
        urlToImage = source_item.get('urlToImage')
        publishedAt = source_item.get('publishedAt')

        if id:
            source_object = Source(id,name,title,description,url,urlToImage,publishedAt)
            source_articles.append(source_object)

    return source_articles
