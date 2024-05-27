from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/showName')
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    name = request.args.get('name')
    
    # Validate name
    if name is None or name == '':
        return make_response('Invalid name', 400)
    
    response = make_response(f'Hello, {name}!', 200)
    return response