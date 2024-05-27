import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    command = request.form.get('command') # Get the command from the post request form data
    if not command: # If the command is not provided, return an error message and a 400 status code
        return "Error: command is required", 400
    else:
        # Validate the command before executing
        # Insert your command validation logic here
        if command.startswith("echo"): # Validate that the command starts with "echo"
            # Execute the command using subprocess and capture the output
            output = os.popen(command).read()
            return output, 200
        else:
            return "Error: Invalid command", 400

if __name__ == '__main__':
    app.run()