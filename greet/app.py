from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return "main page!"

@app.route('/welcome')
def welcome_page():
    return "welcome"

@app.route('/welcome/home')
def welcome_home_page():
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    return 'welcome back'