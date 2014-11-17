from flask import Flask, render_template, request
from analysis import basic
from redis import Redis
from rq import Queue
import settings


app = Flask(__name__)

if settings.enable_background_jobs:
    q = Queue(settings.queue_name, connection=Redis())

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        if settings.enable_background_jobs:
            q.enqueue(basic, **request.json)
        else:
            basic(**request.json)
        return "OK"

if __name__ == "__main__":
    app.debug = True
    app.run()
