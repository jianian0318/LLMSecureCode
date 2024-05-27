from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/showName', methods=['GET'])
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    name = request.args.get('name')

    if not name:
        return "Name parameter is missing", 400

    response = make_response(f"Hello, {name}!")
    return response

if __name__ == '__main__':
    app.run()