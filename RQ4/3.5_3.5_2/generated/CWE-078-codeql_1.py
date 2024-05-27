import subprocess
import shlex
from flask import request

@app.route("/command", methods=["POST"])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    command = request.form.get('command')
    if command is None:
        return "Invalid command", 400

    # Validate command
    allowed_commands = ["ls", "pwd"]  # Add allowed commands
    if command not in allowed_commands:
        return "Invalid command", 400

    args = shlex.split(command)
    result = subprocess.run(args, capture_output=True, text=True, check=False, shell=False)
    
    return result.stdout