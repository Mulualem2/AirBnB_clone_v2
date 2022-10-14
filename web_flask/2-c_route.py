#!/usr/bin/python3
"""Starts Flask web app
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
    /c/<text> - display "C <text>"
"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/')
def hello():
    '''
    Hello route
    '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''
    HBNB route
    '''
    return 'HBNB:'


@app.route('/c/<text>')
def c_text(text):
    '''
    /c/<text> route
    '''
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
