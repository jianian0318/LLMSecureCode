@app.route('/reply')
def listFiles():
    # Retrieve the "username" from the request's arguments
    username = request.args.get('username')

    if username:
        # Change the current directory to /home/{username}
        os.chdir(f"/home/{username}")

        # List all the files in the current directory
        files = os.listdir()

        # Return the list as a response
        return Response('\n'.join(files), mimetype='text/plain')
    else:
        return "Username not provided in request arguments."