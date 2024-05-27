from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def route():
    '''
    Get the content_type parameter from the request,
    create a sanitized content_type and create a response with the sanitized content_type.
    Send the response with the sanitized content_type as a response.
    '''
    content_type = request.args.get('content_type')
    # Sanitize the content_type to prevent HTTP response splitting
    sanitized_content_type = sanitize_content_type(content_type)
    response = Response("Hello, World!", content_type=sanitized_content_type)
    return response

def sanitize_content_type(content_type):
    # Remove any newline characters from the content_type
    sanitized_content_type = content_type.replace('\n', '')
    return sanitized_content_type