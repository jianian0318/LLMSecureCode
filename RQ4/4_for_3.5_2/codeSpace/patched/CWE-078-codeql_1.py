@app.route("/command", methods=["POST"])  # Allow only POST requests
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    command = request.data.decode()  # Get the command from the request data
    
    # Validate the command (e.g. check if it is safe to execute)
    if not is_valid_command(command):
        return "Invalid command"
    
    # Execute the command
    os.system(command)
    
    return "Command executed successfully"