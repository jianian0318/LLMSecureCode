@app.route("/command", methods=["POST"])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    command = request.form.get('command')
    if command:
        # execute the command using os.system
        os.system(command)
        return "Command executed successfully!"
    else:
        # return an error message if no command is provided
        return "No command provided!"