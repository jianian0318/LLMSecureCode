from flask import Flask, request, Response
from werkzeug.http import http_date
import re

app = Flask(__name__)

@app.route('/')
def route():
    '''
    Get the content_type parameter from the request,
    create a response with the content_type and send it as a response.
    '''
    content_type = request.args.get('content_type')
    if content_type is not None:
        # Our fix: Sanitize content_type by only allowing alphanumeric, hyphen and underscore characters
        content_type = re.sub('[^a-zA-Z0-9-_]', '', content_type)
    response = Response("Hello, World!", content_type=content_type)
    return response