#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes: /: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
replace underscore _ symbols with a space
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """display “Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """display “HBNB”"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """Function thant display C followed by text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def secontext(text="is cool"):
    """Function thant display Python followed by text"""
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
