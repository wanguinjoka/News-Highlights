from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source
from ..request import get_articles
from ..models import Article

#views

@main.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''

    #get various categories of new sources
    general = get_source('general')
    business = get_source('business')
    sports = get_source('sports')
    entertainment = get_source('entertainment')


    title = 'SOURCES OF THE LASTEST WORLD NEWS'
    return render_template('index.html', title = title, general = general, business= business, sports=sports, entertainment = entertainment)

@main.route('/articles')
def articles():

    '''
    view article page function that returns the top headlines page and its data
    '''
    topHeadlines = get_articles()
    return render_template('articles.html', topHeadlines=topHeadlines)
