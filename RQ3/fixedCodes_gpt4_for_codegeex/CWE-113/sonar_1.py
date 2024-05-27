from flask import Response, request, Flask
import re

app = Flask(__name__)


@app.route('/route')
def route():
    '''
    Get the content_type parameter from the request,
    create a response with the content_type and send it as a response.
    '''
    content_type = request.args.get('content_type')
    
    # Validate content_type
    if re.search(r'[\r\n]', content_type):
        content_type = 'text/plain'  # default value or return an error

    response = Response(content_type=content_type)
    return response