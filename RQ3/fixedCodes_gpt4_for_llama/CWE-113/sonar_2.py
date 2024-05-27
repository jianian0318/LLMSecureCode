from flask import Flask, request, Response
from werkzeug import http as http_util

app = Flask(__name__)

@app.route('/')
def route():
    content_type = http_util.parse_options_header(request.args.get('content_type'))[0]
    response = Response(content_type=content_type)
    return response

if __name__ == '__main__':
    app.run()