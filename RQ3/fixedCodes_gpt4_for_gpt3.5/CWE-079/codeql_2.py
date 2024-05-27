from flask import Flask, request, make_response
import html

app = Flask(__name__)

@app.route('/showName')
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    name = request.args.get('name')  # Get the value of "name" from the request args
    if not name:  # If name is not provided in the request
        return make_response('Name parameter missing', 400)  # Return a response with a 400 status code and an error message

    # Do validation on the name parameter (e.g. check if it is a valid name)
    
    name = html.escape(name)  # Escape any HTML special characters 

    response_body = f'The name is: {name}'  # Create a response body with the name parameter
    response = make_response(response_body, 200)  # Create a response with a 200 status code
    return response  # Return the response object