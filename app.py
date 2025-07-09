from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dosto, Kya haal chaal kaise ho sab theek?"

@app.route('/health')
def health():
    return 'Server is up and running'
