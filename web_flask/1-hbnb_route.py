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
    """display hbnb!"""
    return "HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
