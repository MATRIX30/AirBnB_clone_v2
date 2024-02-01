#!/usr/bin/python3
"""
python script to start a flask app with the /cities_by_states route
returning all the states and cities stored in storage (file/db storage)
and rendered using jinja template
"""


from flask import Flask, render_template
from models import storage, State, City


app = Flask(__name__)
app.jinja_env.lstrip_blocks = True


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    This is the main function that handles the /states_list route
    """
    state_list = storage.all(State).values()
    city_list = storage.all(City).values()
    return render_template("8-cities_by_states.html",
                           states=state_list, cities=city_list)


@app.teardown_appcontext
def close_storage(error=None):
    """
    method to close and clean database connection
    sessions
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
