from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/showName')
def name():
    '''
    This function handles a GET request at the endpoint '/showName'. It gets "name" from the request parameters,
    validates it, creates a HTTP response that contains this name, and returns this response.
    '''

    # Get "name" from the request
    name = request.args.get('name', '')

    # We add a simple validation to ensure the name is not empty most apps will need more complex checks.
    # If it's empty, we return a response with the error.
    if not bool(name.strip()):
        response = make_response('Name parameter cannot be empty.', 400)
        return response

    # If the name is not empty, we make a response with it using escape to prevent XSS attacks and return the response object.
    response = make_response(f'Hello {escape(name)}!', 200)
    return response