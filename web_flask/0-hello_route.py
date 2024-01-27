#!/usr/bin/python3
"""
scripts that starts a flask web application
with the route / that returns "Hello HBNB"
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Method to run when / route is entered"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
