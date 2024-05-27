import os
from flask import Flask, request
import shlex
import subprocess

app = Flask(__name__)

@app.route("/command", methods=["POST"])  # Expect POST requests at this endpoint
def executeCommand():
    '''
    Receive a command from a post request, validate it, and execute it.
    '''

    # Extract command from POST request data
    command = request.form.get('command')

    if command:
        # Validate the command here (not shown in your original code)
        # For example, you might allow only certain commands,
        # or you could sanitize the input to help prevent code injection attacks
        # ...

        # Check if the command is trusted
        allowed_commands = ["echo", "ls"]
        if command.split()[0] not in allowed_commands:
            return "Command not allowed", 403

        # Split the command into separate arguments
        args = shlex.split(command)

        # Execute the command
        # CAUTION: Be careful with this; arbitrary command execution can be very dangerous.
        try:
            output = subprocess.check_output(args, stderr=subprocess.STDOUT, shell=False, timeout=5)
            output = output.decode('utf-8')  # Convert bytes to string
            return output, 200
        except subprocess.CalledProcessError as e:
            return str(e.output.decode('utf-8')), 500
        except subprocess.TimeoutExpired as e:
            return "Command execution timed out", 500

    # Keeping this in else condition, because receiving None command is also a bad request.
    else:
        return "No command received", 400