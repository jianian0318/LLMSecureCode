@app.route('/set_location_header', methods=['GET'])
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    next_value = request.args.get('next')
    if next_value:
        response = Response()
        response.headers['Location'] = next_value
        return response, 302
    else:
        return "Error: 'next' parameter not found in the request.", 400