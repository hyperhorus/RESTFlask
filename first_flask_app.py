#from flask import Flask
import flask
from flask import Flask

app = Flask(__name__)

x@app.route('/')
def home():
    return 'Hello world! Welcome to the jungle'

#app.run(port=5000)