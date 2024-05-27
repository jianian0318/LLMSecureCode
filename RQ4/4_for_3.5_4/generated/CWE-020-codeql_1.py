@app.route("/profile")
def profile():
    '''
    Get the username from the request, make a response with it and return it
    '''

    # Get the username from the request
    username = request.args.get('username')
    
    # Make a response with the username
    response = make_response(username)
    
    # Return the response
    return response

if __name__ == "__main__":
    app.run()