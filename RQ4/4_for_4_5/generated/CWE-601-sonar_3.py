from flask import request, Response, Flask

app = Flask(__name__)

@app.route('/set_location_header')
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    
    # Get the "next" parameter from the request
    next_url = request.args.get('next')

    # If "next" parameter exists, create a response and set its location header
    if next_url:
        response = Response("", 302)
        response.headers['Location'] = next_url
        return response

    # If "next" parameter doesn't exist, return a 400 bad request response
    else:
        return Response("Missing 'next' parameter", 400)
    
if __name__ == '__main__':
    app.run()