from flask import Flask, request, make_response
from jinja2 import escape

app = Flask(__name__)

@app.route('/showName')
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    name = request.args.get('name', '')
    
    # Apply escaping to user-supplied input to prevent Cross-site Scripting attacks
    name = escape(name)
    
    if not name:
        return make_response('Name not provided', 400)
        
    return make_response(f'Hello, {name}!', 200)

if __name__ == "__main__":
    # Never run the application in debug mode in a production environment
    app.run(debug=False)