from app import app
import urllib.request,json
from .models import source

Source = source.Source

# getting the api key
apiKey = app.config['SOURCE_API_KEY']

#getting the source base urlli
base_url = app.config['NEWS_API_BASE_URL']

def get_source(category):
    '''
    function that gets the json url request
    '''
    get_source_url = base_url.format(category,apiKey)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_articles = None

        if get_source_response['articles']:
            source_articles_list = get_source_response['articles']
            source_articles = process_articles(source_articles_list)

    return source_articles
