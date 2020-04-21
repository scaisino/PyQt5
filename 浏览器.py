# -*-coding：utf-8-*-
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('html.html')


app.run()
