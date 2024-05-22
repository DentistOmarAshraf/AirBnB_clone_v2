#!/usr/bin/python3
"""
Flask Project
"""


from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def slash(text):
    return f"C {text.replace('_',' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def slash_2(text=None):
    if not text:
        return "Python is cool"
    return f"Python {text.replace('_',' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n=None):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def is_num_temp(n=None):
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n=None):
    if int(n % 2) == 0:
        num = f"{n} is even"
    else:
        num = f"{n} is odd"
    return render_template("6-number_odd_or_even.html", number=num)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
