from flask import request, Response, Flask

app = Flask(__name__)

@app.route('/set_location_header')
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    next = request.args.get('next')
    if next:
        response = Response("", status=302)
        response.headers['Location'] = next
        return response
    return "No next parameter provided", 400