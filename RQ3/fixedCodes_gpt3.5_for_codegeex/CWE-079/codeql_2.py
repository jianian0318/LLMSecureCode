from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/showName')
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    name = request.args.get('name')
    if not name or not name.isalpha():
        return make_response('Invalid name', 400)
    return make_response(f'Hello, {escape(name)}!', 200)