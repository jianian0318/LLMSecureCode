@app.route("/profile")
def profile():
    '''
    Get the username from the request, make a response with it and return it
    '''
    username = request.args.get('username')  # Get the username from the request parameters
    response = make_response(username)  # Create a response with the username
    return response  # Return the response