#!/usr/bin/python3

"""
 starts a Flask web application
"""

from flask import Flask, render_template
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


# routing the decorator function ami_a_number
@app.route('/number/<int:n>', strict_slashes=False)
def ami_a_number(n):
    """display python with a text"""
    return "{} is a number".format(n)


# routing the decorator function number_template
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


# routing the decorator function odd_or_even
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """display HTML page only if n is an integer"""
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html",
                               m="{} is even".format(n))
    else:
        return render_template("6-number_odd_or_even.html",
                               m="{} is odd".format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
