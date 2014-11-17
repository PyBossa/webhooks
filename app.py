import json
import enki
import settings
from flask import Flask, render_template, request
from analysis import basic
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        basic(**request.json)
        return "OK"

if __name__ == "__main__":
    app.debug = True
    app.run()
