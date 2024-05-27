@app.route('/set_location_header', methods=['GET'])
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    next_url = request.args.get('next')
    if next_url:
        response = Response()
        response.headers['Location'] = next_url
        return response, 302
    else:
        return 'Missing next URL parameter', 400