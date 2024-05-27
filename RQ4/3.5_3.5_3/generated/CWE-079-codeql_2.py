@app.route('/showName', methods=['GET'])
def show_name():
    # Get the value of the "name" parameter from the request
    name = request.args.get('name')

    # Check if "name" exists and is valid
    if name is None or name == '':
        # Return a bad request response if "name" is missing or empty
        return make_response('Invalid name', 400)

    # Create a response object with the name
    response_text = f'Your name is {name}'
    response = make_response(response_text, 200)

    # Return the response object
    return response