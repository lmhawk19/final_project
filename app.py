from flask import Flask, render_template
from helpers import get_random_suggestion_list
app = Flask(__name__)

#put class here
#pass it down to the .gets
#post requests, use some javascript, send data from json/javascript to an end point
#use mySQL or mySQLlite to connect a database


@app.get('/')
def languages_app():
    return '<h1>Welcome to our DIY Couples Therapy App!</h1><p>Our randomised, love language-based suggestions are here to help you be better partners.</p>'

@app.get('/languages')
def languages_list():
    random_suggestion_list = get_random_suggestion_list()
    return render_template('languages_list.html', suggestion_list = random_suggestion_list)

@app.get('/languages/<int:language_id>')
def language_info(language_id):
    return f'You have selected love language {language_id}'










app.run()
