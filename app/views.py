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
    general = get_source('general')
    business = get_source('business')
    sports = get_source('sports')
    entertainment = get_source('entertainment')


    title = 'SOURCES OF THE LASTEST WORLD NEWS'
    return render_template('index.html', title = title, general = general, business= business, sports=sports, entertainment = entertainment)

@app.route('/source/<int:source_id>')
def source(source_id):

    '''
    view article page function that returns the source details page and its data
    '''
    return render_template('source.html',id = source_id)
