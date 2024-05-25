#!/usr/bin/python3
"""
Fetching data from Mysql DB
"""

from flask import Flask
from flask import render_template
import sys
import os
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exeption):
    """remove sql session after each requests"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    """rendering state_id and state_name"""
    all_states = storage.all(State)  # {"stateName.id" : <state_obj>}

    data = {}
    for k, v in all_states.items():
        state_id = k.split(".")[1]
        state_name = v.name
        data[state_id] = state_name

    data = dict(sorted(data.items(), key=lambda item: item[1]))

    return render_template("7-states_list.html", data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
