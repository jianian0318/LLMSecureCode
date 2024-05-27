from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/showName')
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    name = request.args.get('name')
    if not name:
        return make_response('Please provide a name', 400)
    name = escape(name)
    response = make_response(f'Hello {name}!', 200)
    return response

if __name__ == '__main__':
    app.run()