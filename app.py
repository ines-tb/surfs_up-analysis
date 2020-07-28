from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "Hello World"

    
@app.route("/data/")
def dataRoute():
    return "We are inside data route"