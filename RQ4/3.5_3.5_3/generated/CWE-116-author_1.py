@app.route('/reply')
def listFiles():
    # Retrieve the "username" from the request's arguments
    username = request.args.get('username')

    # Change the current directory to /home/{username}
    os.chdir(f'/home/{username}')

    # List all the files in the current directory
    file_list = os.listdir()

    # Return the list as a response
    return Response('\n'.join(file_list), mimetype='text/plain')