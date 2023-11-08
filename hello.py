from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/emily")
def hello_emily_world():
    return "<p>Hello, Emily's world!</p>"