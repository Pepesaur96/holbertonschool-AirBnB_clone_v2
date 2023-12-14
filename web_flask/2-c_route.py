#!/usr/bin/python3
"""starts a Flask web application listening on
0.0.0.0, port 5000 and routes /: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display "C" + text (replaces underscores with spaces)"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display text"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """display custom text given"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
