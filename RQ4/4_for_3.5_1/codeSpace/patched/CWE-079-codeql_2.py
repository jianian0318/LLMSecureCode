from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/showName', methods=['GET'])
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    name = request.args.get('name')  # get the "name" from the query parameters
    if name:  # check if name is not None or an empty string
        response = make_response(f"Hello {name}!")  # create the response with name
        response.status_code = 200  # set the response status code to 200 (OK)
    else:
        response = make_response("Invalid name", 400)  # create a response with error message and status code 400 (Bad Request)
    return response