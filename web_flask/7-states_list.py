#!/usr/bin/python3

"""
 starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import state
from sqlalchemy.orm import scoped_session, sessionmaker

"""instance of the flask class"""
app = Flask(__name__)


"""After each request you must remove the current SQLAlchemy Session"""


@app.teardown_appcontext
def teardown(exception):
    """Closes the current SQLAlchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML page with a list of all State objects"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
