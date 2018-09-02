from app import app
import urllib.request,json
from .models import Source
from .models import Article

# getting the api key
apiKey = None

#getting the source base urlli
base_url = None

#getting the article url
articleBase_url = None

def configure_request(app):
    global apiKey,base_url,articleBase_url
    apiKey = app.config['SOURCE_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    articleBase_url = app.config['ARTICLE_API_BASE_URL']

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

def get_articles():

    '''
    function that gets the json response to our urlrequest
    '''
    get_article_url = articleBase_url.format(apiKey)

    with urllib.request.urlopen(get_article_url)as url:
        get_articles_data =url.read()
        get_articles_response = json.loads(get_articles_data)

        article_articles = None

        if get_articles_response['articles']:
            article_articles_list = get_articles_response['articles']
            article_articles = process_articles(article_articles_list)

    return article_articles

def process_articles(article_list):

    '''
    function that process the articles in api and transform them to a list of objects

    args:
    article_list is a dic that contains article objects

    returns:
    article_articles is a list of article objects
    '''
    article_articles =[]
    for article_item in article_list:
        source = article_item.get('source.id')
        author = article_item.get('author')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

    return article_articles
