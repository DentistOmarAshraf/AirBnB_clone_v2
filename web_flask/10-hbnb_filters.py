#!/usr/bin/python3
"""
Rendiering Page by flask
"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def testing():
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    all_data = {}
    for st in states:
        city = st.cities
        city = sorted(city, key=lambda city: city.name)
        all_data[st] = city

    amen = sorted(list(storage.all(Amenity).values()), key=lambda x: x.name)

    return render_template("10-hbnb_filters.html", data=all_data, amen=amen)


@app.teardown_appcontext
def close_db(exception=None):
    """session elemenation"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
