from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def route():
    '''
    Get the content_type parameter from the request,
    create a response with the content_type after sanitizing it and send it as a response.
    '''
    content_type = request.args.get('content_type')
    sanitized_content_type = sanitize_input(content_type)
    response = Response(content_type=sanitized_content_type)
    return response

def sanitize_input(input_data):
    '''
    Sanitize the input data by removing any newline characters.
    '''
    return input_data.replace('\n', '')

if __name__ == '__main__':
    app.run()