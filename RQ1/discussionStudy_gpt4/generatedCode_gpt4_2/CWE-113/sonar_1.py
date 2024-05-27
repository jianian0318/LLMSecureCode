from flask import Response, request, Flask
from werkzeug.datastructures import Headers

app = Flask(__name__)

@app.route('/route')
def route():
    # Getting the content_type parameter from the request
    content_type = request.args.get('content_type')

    # Creating a response with the content_type and sending it as a response
    headers = Headers()
    headers.add('Content-Type', content_type)

    response = Response(response="Your response goes here", headers=headers)
    
    return response

if __name__ == "__main__":
    app.run(debug=True)