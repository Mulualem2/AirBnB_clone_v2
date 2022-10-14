#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb_filters: HBnB HTML filters page.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filter_hbnb():
    '''
    Display page from static and
    make it interactive
    '''
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()

    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_app(e):
    '''
    teardown app context
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
