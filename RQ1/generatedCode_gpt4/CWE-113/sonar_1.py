from flask import Response, request, Flask
from werkzeug.datastructures import Headers

app = Flask(__name__)


@app.route('/route')
def route():
    # Get the content_type parameter from the request
    content_type = request.args.get('content_type', '')

    # create a response with the content_type and send it as a response.
    headers = Headers()
    headers.add('Content-Type', content_type)
    response = Response(response="Okay", status=200, headers=headers)
    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True)