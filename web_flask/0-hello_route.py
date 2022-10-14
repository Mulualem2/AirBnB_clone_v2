#!/usr/bin/python3
"""Starts Flask web app
Listening on 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    '''
    Hello Flask route
    '''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run()
    app.url_map.strict_slashes = False
