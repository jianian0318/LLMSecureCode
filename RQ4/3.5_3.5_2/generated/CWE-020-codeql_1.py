@app.route("/profile")
def profile():
    username = request.args.get('username')  # get the username from the request args
    response = make_response(username)  # create a response with the username
    return response  # return the response