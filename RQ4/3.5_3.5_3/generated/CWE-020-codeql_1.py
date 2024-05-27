@app.route("/profile", methods=['GET'])
def profile():
    '''
    Get the username from the request, make a response with it and return it
    '''
    username = request.args.get('username') # get the username from the request query parameters
    response = make_response(username) # create a response with the username
    return response # return the response