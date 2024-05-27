from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/showName', methods=['GET'])
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    name = request.args.get('name', default = None)  # extract 'name' from request
    if name:  # validate 'name'
        response = make_response('Hello, {}'.format(name), 200)  # make a response with 'name'
    else:
        response = make_response('No name provided', 400)  # make a response if no 'name' provided
    return response  # return the response object