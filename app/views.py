from flask import render_template
from app import app
from .request import get_source

#views

@app.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''

    #get bbc source
    bbc = get_source('bbc-news')
    abc = get_source('abc-news')
    cbs = get_source('cbs-news')
    cnn = get_source('cnn')
    fox = get_source('fox-news')

    title = 'SOURCES OF THE LASTEST WORLD NEWS'
    return render_template('index.html', title = title, bbc = bbc, abc =abc, cbs =cbs, cnn=cnn, fox = fox)

@app.route('/source/<int:source_id>')
def source(source_id):

    '''
    view article page function that returns the source details page and its data
    '''
    return render_template('source.html',id = source_id)
