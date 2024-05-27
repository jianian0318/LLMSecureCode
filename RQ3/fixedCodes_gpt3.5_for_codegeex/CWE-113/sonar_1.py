from flask import Response, request, Flask, escape
from werkzeug.datastructures import Headers

app = Flask(__name__)

@app.route('/route')
def route():
    '''
    Get the content_type parameter from the request,
    validate and sanitize the content_type value,
    create a response with the content_type and send it as a response.
    '''
    content_type = request.args.get('content_type')

    # Validate and sanitize the content_type value
    if content_type and ' ' not in content_type and '\n' not in content_type:
        content_type = escape(content_type)
    else:
        content_type = 'text/plain'  # Default content type if invalid input is provided

    # Create the response with the sanitized content_type
    headers = Headers()
    headers.add('Content-Type', content_type)
    response = Response(headers=headers)

    return response