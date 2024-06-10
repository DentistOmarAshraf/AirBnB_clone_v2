#!/usr/bin/python3
"""
Flask Project
"""


from flask import Flask


app = Flask("0-hello_route")
app.config['ENV'] = 'production'


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
