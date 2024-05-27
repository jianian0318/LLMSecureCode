@app.route("/command", methods=['POST'])
def executeCommand():
    # Receive the command from the post request
    command = request.form.get('command')
    
    # Validate the command
    if not command:
        return "No command provided", 400
    
    # Execute the command using the 'os.system' function
    os.system(command)
    
    return "Command executed successfully", 200