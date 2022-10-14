#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states_by_id(state_id=None):
    '''
    Lists states by the state id
    and cities in that state
    '''
    states = storage.all('State')
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html',
                           states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_app(e):
    '''
    teardown app context
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
