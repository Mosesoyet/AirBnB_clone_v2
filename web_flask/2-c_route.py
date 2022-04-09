#!/usr/bin/python3
"""
Start a Flask application which listen on 0.0.0.0 port 500
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """returns string to the route'"""
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB to the /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun():
    """returns a string to the c/<text> route"""
    new = text.replace('_', ' ')
    return 'C %s' % new


if __name__=='__main__':
    app.run(host='0.0.0.0')
