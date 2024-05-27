from flask import request, Response, Flask

app = Flask(__name__)

@app.route('/set_location_header')
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    next_url = request.args.get('next')  # Getting the 'next' value from the request
    if next_url is not None:  # If 'next' value exists
        response = Response()  # Create a blank response
        response.headers['Location'] = next_url  # Set the location header
        return response  # Returning the response with the location header
    return Response("No 'next' url to redirect.", status=400)  # Returning an error message if 'next' value does not exist