#!/usr/bin/python3
"""Start a Flask application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """returns a string to the route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns a string to the /hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun():
    """returns a string to the /c/<text> route"""
    new = text.replace("_", " ")
    return "C %s" % new


@app.route('/python/(<text>)', strict_slashes=False)
def python_iscool():
    """returns a string to the /python/(<text>) route"""
    nw = text.replace("_", " ")
    return "Python %s" % nw


if __name__=="__main__":
    app.run(host="0.0.0.0")
