#!/usr/bin/python3
"""
starts a Flask web application listening on
0.0.0.0, port 5000 and routes /: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display "C" + text (replaces underscores with spaces)
/python/(<text>): display "Python" + text (default is 'is cool')
/number/<n>: display "n is a number" only if n is an integer
/number_template/<n>: display HTML page only if n is an integer
/number_odd_or_even/<n>: display HTML page only if n is an integer
/state_list: display HTML page with list of all State objects
/cities_by_states: display HTML page with list of all City objects
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """Display a HTML page with list of all State objects"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('states.html', states=states)


@app.route('/states/<id>')
def states_id(id):
    """Display a HTML page with list of all City objects linked to the State"""
    state = storage.get(State, id)
    if state is not None:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('states_id.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
