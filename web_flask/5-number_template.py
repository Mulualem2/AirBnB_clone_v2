#!/usr/bin/python3
"""Starts Flask web app
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
    /c/<text> - display "C <text>"
    /python/<text> - display "Python is cool"
    /number/<n> - display n if integer
    /number_template/<n> - display a HTML page if n is int
"""
from flask import Flask, escape, render_template
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


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    '''
    /python/<text> route
    '''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_route(n):
    '''
    /number/<n> route
    '''
    return '{} is a number'.format(int(n))


@app.route('/number_template/<int:n>')
def number_template(n):
    '''
    /number_template/<n> route
    '''
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
