#!/usr/bin/python3
"""
scripts that starts a flask web application
with the route / that returns "Hello HBNB"
"""
from flask import Flask, abort, render_template

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


@app.route("/python/<string:text>",  strict_slashes=False)
@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
def python_is_cool(text):
    return "Python " + text.replace('_', ' ')


@app.route("/number/<n>", strict_slashes=False)
def is_number(n):
    print(type(n))
    if n.isdigit():
        return f"{n} is a number"
    return abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    data = n
    if n.isdigit():
        return render_template('5-number.html', n=n)
    return abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
