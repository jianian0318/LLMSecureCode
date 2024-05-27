@app.route('/showName')
def name():
    # Get "name" from the request
    name = request.args.get('name')

    # Validate the name
    if not name:
        # If the name is not provided, return an error response
        response = make_response('Name is missing', 400)
    else:
        # Make a response with the name
        response = make_response(f'Hello, {name}!')

    # Return the response object
    return response