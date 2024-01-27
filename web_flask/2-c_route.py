#!/usr/bin/python3
"""
scripts that starts a flask web application
with the route / that returns "Hello HBNB"
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Method to run when / route is entered"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Method to run when /hbnb route is entered"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c_is_fun(text):
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
