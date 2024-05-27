from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/set_location_header', methods=['GET'])
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    next_url = request.args.get('next')
    if next_url:
        response = Response()
        response.headers['Location'] = next_url
        response.status_code = 302
        return response
    else:
        return Response(status=400)  # Bad Request if "next" parameter is missing