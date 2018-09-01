from flask import render_template
from app import app
from .request import get_source
from .request import get_articles

#views

@app.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''

    #get bbc source
    general = get_source('general')
    business = get_source('business')
    sports = get_source('sports')
    entertainment = get_source('entertainment')


    title = 'SOURCES OF THE LASTEST WORLD NEWS'
    return render_template('index.html', title = title, general = general, business= business, sports=sports, entertainment = entertainment)

@app.route('/article')
def articles():

    '''
    view article page function that returns the top headlines page and its data
    '''
    topHeadlines = get_articles()
    return render_template('articles.html', topHeadlines=topHeadlines)
