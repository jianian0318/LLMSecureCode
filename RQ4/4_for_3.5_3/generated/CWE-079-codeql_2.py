@app.route('/showName', methods=['POST'])
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    name = request.form.get('name')
    
    # Validate name
    if name is None or len(name) == 0:
        return make_response('Invalid name', 400)
    
    response = make_response(name)
    return response