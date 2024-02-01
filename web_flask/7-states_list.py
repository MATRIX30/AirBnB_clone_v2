#!/usr/bin/python3
"""
python script to start a flask app with the /states_list route
returning all the states stored in storage (file/db storage)
and rendered using jinja template
app.jinja_env.lstrip_blocks = True
"""

from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    This is the main function that handles the /states_list route
    """
    state_list = storage.all(State).values()
    return render_template("7-states_list.html", states=state_list)


@app.teardown_appcontext
def close_storage(error=None):
    """
    method to close and clean database connection
    sessions
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
