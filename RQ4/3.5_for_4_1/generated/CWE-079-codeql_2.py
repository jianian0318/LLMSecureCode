from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/showName')
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    # Get "name" from the request
    name = request.args.get('name')
    
    # Validate "name"
    if name is None or name.strip() == '':
        response = make_response("No name provided", 400)
    else:
        # Make a response with "name" and return the response object
        response = make_response("Hello, " + escape(name), 200)
    
    return response

if __name__ == '__main__':
    app.run()