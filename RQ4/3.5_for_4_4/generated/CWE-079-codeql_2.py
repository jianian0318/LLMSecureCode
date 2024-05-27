from flask import Flask, request, make_response, escape

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/showName', methods=['GET'])
def name():
    """
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    """
    name = request.args.get('name', default='No name provided', type=str)
    if name:
        escaped_name = escape(name)
        response = make_response(f'Hello, {escaped_name}', 200)
        return response
    else:
        response = make_response('Name parameter not found.', 400)
        return response

if __name__ == "__main__":
    app.run()