from flask import Response, request, Flask
from werkzeug.datastructures import Headers

app = Flask(__name__)

@app.route('/route')
def route():
    # Get the content_type parameter from the request
    content_type = request.args.get('content_type', default = "*", type = str)
    
    # Create a response with the content_type
    headers = Headers()
    headers.add('Content-Type', content_type)
    response = Response(response="Your response goes here", headers=headers)

    # Send it as a response.
    return response

if __name__ == '__main__':
    app.run()