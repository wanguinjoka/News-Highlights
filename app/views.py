from flask import render_template
from app import app

#views

@app.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''
    message = 'Flash new'
    return render_template('index.html',message = message)

# @app.route('/articles/<_id>')
# def source(source_id):
#
#     '''
#     view article page function that returns the articles details page and its data
#     '''
#     return render_template('source.html',id = source)
