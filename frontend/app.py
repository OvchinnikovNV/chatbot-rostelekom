from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
def neural_network():
    pass


if __name__ == '__main__':
    app.run(debug=True)
