from flask import Flask, request, make_response
from jinja2 import escape

app = Flask(__name__)

@app.route('/showName')
def name():
    name = request.args.get('name')
    if name:
        safe_name = escape(name)
        response = make_response(safe_name)
    else:
        response = make_response('Invalid name')
    return response

if __name__ == '__main__':
    app.run()