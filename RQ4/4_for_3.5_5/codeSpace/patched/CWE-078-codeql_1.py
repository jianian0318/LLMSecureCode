@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    command = request.form.get('command')
    
    # Validate the command
    valid_commands = ['command1', 'command2', 'command3']
    if command not in valid_commands:
        return "Invalid command"
    
    # Execute the command
    os.system(command)
    return "Command executed successfully"