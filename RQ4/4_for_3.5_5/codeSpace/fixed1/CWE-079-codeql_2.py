from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/showName')
def name():
    '''
    Get "name" from the request, validate it, escape any HTML special characters to prevent XSS,
    make a response with it, and return the response object
    '''
    name = request.args.get('name')
    
    # Validate name
    if name is None or name == '':
        return make_response('Invalid name', 400)
    
    # Escape name to prevent cross-site scripting (XSS)
    escaped_name = escape(name)
    
    response = make_response(f'Hello, {escaped_name}!', 200)
    return response