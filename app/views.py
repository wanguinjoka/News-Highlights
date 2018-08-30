from flask import render_template
from app import app

#views

@app.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''
    title = 'HOME - LASTEST WORLD NEW'
    return render_template('index.html', title = title)

@app.route('/source/<int:source_id>')
def source(source_id):

    '''
    view article page function that returns the source details page and its data
    '''
    return render_template('source.html',id = source_id)
