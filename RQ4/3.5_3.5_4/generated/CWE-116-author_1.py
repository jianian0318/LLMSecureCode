@app.route('/reply')
def listFiles():
    username = request.args.get('username')  # Retrieve the "username" from the request's arguments
    os.chdir(f'/home/{username}')  # Change the current directory to /home/{username}
    files = os.listdir()  # List all the files
    
    return Response('\n'.join(files), mimetype='text/plain')  # Return the list as a response