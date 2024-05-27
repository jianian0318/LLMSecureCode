from flask import request, Response, Flask

app = Flask(__name__)


@app.route('/set_location_header', methods=['GET'])
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    next_url = request.args.get('next')  # Get the value of "next" from the query parameters
    if next_url:  # If "next" value exists
        response = Response()
        response.headers['Location'] = next_url  # Set the location header to the value of "next"
        response.status_code = 302  # Set the status code to 302 (Found/Redirect)
        return response
    else:
        return 'Missing "next" parameter', 400

if __name__ == '__main__':
    app.run()