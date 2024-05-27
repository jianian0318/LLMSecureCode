from flask import Flask, request, make_response
import cgi

app = Flask(__name__)

@app.route('/showName', methods=['GET'])
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    name = request.args.get('name')  # get the "name" from the query parameters
    
    # Input validation and handling
    if name: 
        # escape inputs for HTML to prevent XSS
        name = cgi.escape(name) 
        response = make_response(f"Hello {name}!")  # create the response with name
        response.status_code = 200  # set response status code to 200 (OK)
    else:
        response = make_response("Invalid name", 400)  # create a response with error message and status code 400 (Bad Request)
    return response