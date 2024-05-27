from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/showName', methods=['GET'])
def name():
    '''
    Get "name" from the request, sanitize it with escape(),
    make a response with it, and return the response object
    '''
    name = request.args.get('name')

    if not name:
        return "Name parameter is missing", 400
    
    # Escape special HTML characters to prevent XSS
    safe_name = escape(name)

    response = make_response(f"Hello, {safe_name}!")
    return response

if __name__ == '__main__':
    app.run()