import requests


def generate_word_cloud(text):
    response = requests.get(f"https://quickchart.io/wordcloud?text={text}&scale=sqrt&maxNumWords=30&removeStopwords=true")
    return response.text
