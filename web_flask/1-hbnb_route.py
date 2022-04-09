#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strick_slashes=False)
def hello_school():
    """Returns a string"""
    return 'Hello HBNB!'


@app.route('/hbnb', strick_slashes=False)
def hbnb():
    """Returns a string to /hbnb route"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
