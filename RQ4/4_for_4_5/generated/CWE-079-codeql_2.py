from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/showName')
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    # Get name from the request
    name = request.args.get('name', '')

    # Validate name
    if not name:
        return make_response('No name provided.', 400)

    # Make a response with the name
    response = make_response('Hello, {}!'.format(name), 200)

    # Return the response object
    return response