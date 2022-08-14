from flask import Flask, request, render_template, redirect
import love_languages
import word_cloud_api

app = Flask(__name__)

words_of_affirmation = love_languages.WordsOfAffirmation()
quality_time = love_languages.QualityTime()
acts_of_service = love_languages.ActsOfService()
receiving_gifts = love_languages.ReceivingGifts()
physical_touch = love_languages.PhysicalTouch()

all_love_languages = [
    words_of_affirmation,
    quality_time,
    acts_of_service,
    receiving_gifts,
    physical_touch,
]


@app.get('/')
def home():
    return render_template('home.html', love_languages=all_love_languages)


@app.get('/suggest')
def view_suggestion_form():
    return render_template('suggest.html', love_languages=all_love_languages)


@app.post('/suggest')
def submit_suggestion_form():
    name = request.form.get('name')
    suggestion = request.form.get('suggestion')
    category = request.form.get('category')
    url = request.form.get('url')
    love_languages.add_suggestion(name, suggestion, category, url)
    return redirect('/')


@app.get('/languages/words_of_affirmation')
def view_words_of_affirmation():
    return render_template('love_language.html', love_language=words_of_affirmation)


@app.get('/languages/quality_time')
def view_quality_time():
    return render_template('love_language.html', love_language=quality_time)


@app.get('/languages/acts_of_service')
def view_acts_of_service():
    return render_template('love_language.html', love_language=acts_of_service)


@app.get('/languages/receiving_gifts')
def view_receiving_gifts():
    return render_template('love_language.html', love_language=receiving_gifts)


@app.get('/languages/physical_touch')
def view_physical_touch():
    return render_template('love_language.html', love_language=physical_touch)


@app.get('/data')
def view_data():
    word_clouds = {love_language.name: word_cloud_api.generate_word_cloud(' '.join(love_language.get_all_suggestions()))
                   for love_language in all_love_languages}
    return render_template('data.html', word_clouds=word_clouds)


app.run()
