from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dosto, Kya Haal chall'

@app.route('/health')
def health():
    return 'Server is up and running'
