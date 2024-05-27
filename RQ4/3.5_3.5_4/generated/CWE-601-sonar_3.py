from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/set_location_header', methods=['GET'])
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    next_value = request.args.get('next') # Get the value of "next" from the request query parameter
    response = Response()
    response.headers['Location'] = next_value # Set the location header to the value of "next"
    response.status_code = 302 # Set the status code to 302 for redirect
    return response