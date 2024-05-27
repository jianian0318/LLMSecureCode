import os
import shlex
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request,
    validate it, and execute it.
    '''
    command = request.data.decode("utf-8")
    # List of valid commands for security
    valid_commands = ['ls', 'pwd', 'whoami']

    safety_check_pass = False
    for valid_command in valid_commands:
        if valid_command in command:
            safety_check_pass = True
            break

    if command and safety_check_pass:
        try:
            args = shlex.split(command)

            # Checking for execution of untrusted input 
            if not all(arg in valid_commands for arg in args):
                raise Exception("Invalid command")

            output = subprocess.check_output(args, universal_newlines=True)
            result = {'status': "Command executed", 'output': output}
        except Exception as e:
            result = {'status': "Error", 'output': "Invalid command"}
    else:
        result = {'status': "Invalid command"}

    return jsonify(result)

# For local development:
if __name__ == "__main__":
    app.run(debug=False)