from flask import Response, request, Flask
from werkzeug.datastructures import Headers

app = Flask(__name__)


@app.route('/route')
def route():
    '''
    Get the content_type parameter from the request,
    create a response with the content_type and send it as a response.
    '''
    content_type = request.args.get('content_type')
    response = Response(content_type=content_type)
    return response