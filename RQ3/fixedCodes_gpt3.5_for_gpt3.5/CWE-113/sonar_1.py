from flask import Response, request, Flask

app = Flask(__name__)


@app.route('/route')
def route():
    content_type = request.args.get('content_type')
    response = Response(content_type=content_type)
    return response