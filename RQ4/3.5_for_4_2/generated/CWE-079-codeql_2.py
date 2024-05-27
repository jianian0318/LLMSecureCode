from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.route('/showName', methods = ['POST'])
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    # Get name from the request
    name = request.json.get('name')

    # Validate it
    if not name:
        return make_response(jsonify({'error': 'Name is required'}), 400)
    
    # Make a response with it
    response = make_response(jsonify({'name': name}))

    # Return the response object
    return response