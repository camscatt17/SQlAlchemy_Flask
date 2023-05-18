from application import app
from flask import request
import json 

def response_to_front(result):
    return app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/jason'
    )

def date_format(**kwargs):
    if 'date' in kwargs:
        kwargs['date'] = kwargs['date'].strftime('%Y-%m-%d %H:%M:%S')
    return kwargs

@app.route("/")
@app.route("/index")
def index():
    return "Hello from Flask!"

app.run(debug=True)