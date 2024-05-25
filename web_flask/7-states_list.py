#!/usr/bin/python3
"""
Fetching data from Mysql DB
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    rendering state_id and state_name
    """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template("7-states_list.html", data=states)


@app.teardown_appcontext
def close_db(exeption=None):
    """
    remove sql session after each requests
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
