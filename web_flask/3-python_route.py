#!/usr/bin/python3
"""
Flask Project
"""


from flask import Flask


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


@app.route("/python/<text>", strict_slashes=False)
def slash_2(text):
    return f"Python {text.replace('_',' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
