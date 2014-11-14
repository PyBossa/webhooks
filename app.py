import json
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        with open('./static/results.json', 'w') as f:
            f.write(json.dumps(request.json))
        return "OK"

if __name__ == "__main__":
    app.debug = True
    app.run()
