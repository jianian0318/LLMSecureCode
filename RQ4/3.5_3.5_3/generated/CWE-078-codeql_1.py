import os
from flask import Flask, request
import subprocess
import shlex

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    if request.method == 'POST':
        command = request.form.get('command')  # assuming the command is passed as a form parameter named 'command'

        # Validate the command if needed
        if command is not None and command != '':
            # Validate the command to prevent code injection
            valid_command = validate_command(command)
            if valid_command:
                # Execute the command using subprocess Popen with shell=False
                process = subprocess.Popen(shlex.split(valid_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                output = stdout.decode() if stdout else stderr.decode()

                # Return the result of the command execution
                return f"Command executed. Result: {output}"
            else:
                return "Invalid command"

    return "Invalid request"


def validate_command(command):
    '''
    Validate the command by checking for untrusted input or any suspicious characters.
    Returns the validated command or None if the command is invalid.
    '''
    valid_command = command.strip()

    # Check for any suspicious characters in the command
    suspicious_characters = [';', '&', '|', '`', '$', '(', ')', '<', '>', '\\', '\n']
    if any(suspicious_character in valid_command for suspicious_character in suspicious_characters):
        return None

    return valid_command


if __name__ == "__main__":
    app.run()