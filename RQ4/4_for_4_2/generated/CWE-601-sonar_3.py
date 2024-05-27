from flask import request, Response, Flask

app = Flask(__name__)

@app.route('/set_location_header')
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    next_location = request.args.get('next')
    if next_location:
        response = Response()
        response.headers['Location'] = next_location
        return response
    else:
        return "No 'next' argument provided!", 400