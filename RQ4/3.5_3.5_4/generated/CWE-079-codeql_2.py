@app.route('/showName')
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    # Get the "name" parameter from the request
    name_param = request.args.get('name')

    # Check if the "name" parameter exists and is not empty
    if name_param is None or name_param == '':
        # Return a response with a 400 status code and an error message
        return make_response('Invalid name parameter', 400)

    # Create a response with the name parameter
    response = make_response(name_param)

    # Return the response object
    return response