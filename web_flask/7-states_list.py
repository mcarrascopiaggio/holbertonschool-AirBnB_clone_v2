#!/usr/bin/python3
"""Write a script that starts a Flask web application:
You must use storage for fetching data from the storage engine (FileStorage or
DBStorage) => from models import storage and storage.all(...)
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
Routes: /states_list: display a HTML page: (inside the tag BODY)

"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """Closing DB"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displaying list of states"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
