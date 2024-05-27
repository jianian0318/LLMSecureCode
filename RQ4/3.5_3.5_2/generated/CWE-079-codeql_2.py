@app.route('/showName', methods=['GET'])
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    name = request.args.get('name')
    
    if name is None or not name.isalpha():
        return make_response('Invalid name', 400)
    
    response = make_response(f'Hello, {name}!', 200)
    return response

if __name__ == '__main__':
    app.run(debug=True)