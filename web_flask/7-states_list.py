#!/usr/bin/python3
"""
scripts that starts a flask web application
with the route /states_list returning all states in
database
"""
from flask import Flask, abort, render_template
from models import storage
from models import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """method to list all the states in storage"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session(exception=None):
    """
    method to close the session and close connection to storage
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
