#!/usr/bin/python3
"""
fetching Data from Mysql DB
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception=None):
    """Close Mysql session"""
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """render all states page"""
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)

    if id:
        for st in states:
            if id == st.id:
                city = st.cities
                city = sorted(city, key=lambda city: city.name)
                return render_template("9-states.html", st_id=id,  data=st,
                                       city=city, found=True)

        return render_template("9-states.html", st_id=id, found=False)

    return render_template("9-states.html", st_id=None, data=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
