#!/usr/bin/python3

"""
 starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


# routing the decorator function hello_hbnb
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display hello hbnb!"""
    return "Hello HBNB!"


# routing the decorator function hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display hbnb"""
    return "HBNB"


# routing the decorator function c_text
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display C with a text"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


# routing the decorator function python_text
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """display python with a text"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
