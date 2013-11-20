from flask import Flask, request, render_template
import re
import json

app = Flask(__name__)


def de_lucas(text):
    with open('words.json') as json_data:
        words = json.load(json_data)

    for word in words:
        text = text.replace(word,words[word])

    return text


@app.route('/')
def show_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def show_answer():
    text = request.form['text']
    return de_lucas(text)


if __name__ == '__main__':
    app.debug=True
    app.run(host='119.252.27.58')
