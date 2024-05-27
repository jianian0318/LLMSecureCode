import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request,
    validate it, and execute it.
    '''
    command = request.form.get('command')
    if validateCommand(command):
        result = subprocess.run(command.split(), text=True, capture_output=True)
        return result.stdout
    else:
        return "Invalid command"

def validateCommand(command):
    '''
    Validate the command to ensure it's safe and doesn't contain any malicious code.
    '''
    # Define a whitelist of allowed commands
    allowed_keywords = ['echo', 'ls', 'cd', 'pwd']

    # Check if the command is in the whitelist
    command_word = command.split()[0]
    if command_word not in allowed_keywords:
        return False

    # If the command passes all checks, return True
    return True


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)