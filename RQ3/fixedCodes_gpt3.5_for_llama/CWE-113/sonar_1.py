from flask import Response, request, Flask, escape
from werkzeug.datastructures import Headers

app = Flask(__name__)


@app.route('/route')
def route():
    content_type = request.args.get('content_type')
    content_type = escape(content_type)
    response = Response(headers=Headers({'Content-Type': content_type}))
    return response


if __name__ == '__main__':
    app.run()