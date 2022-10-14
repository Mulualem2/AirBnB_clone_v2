#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    '''
    Lists cities by the state
    it is in
    '''
    state_dict = storage.all('State')
    state_list = []
    for state in state_dict.values():
        state_list.append(state)
    return render_template('8-cities_by_states.html', state_list=state_list)


@app.route('/states_list', strict_slashes=False)
def list_states():
    '''
    Lists states from db
    '''
    state_dict = storage.all('State')
    state_list = []

    for state in state_dict.values():
        state_list.append(state)
    return render_template('7-states_list.html', state_list=state_list)


@app.teardown_appcontext
def teardown_app(e):
    '''
    teardown app context
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
