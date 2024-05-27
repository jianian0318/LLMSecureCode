import shlex
import subprocess
from flask import Flask, request

app = Flask(__name__)

VALID_COMMANDS = ["ls", "pwd", "date", "uname"]  # Define a list of valid commands that you allow.

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request,
    validate it, and execute it.
    '''

    requestData = request.get_json()
    if requestData is None:
        return "Invalid command", 400

    if 'command' not in requestData:
        return "No command provided", 400

    command = requestData.get('command')

    # Validate the command
    command_parts = shlex.split(command)
    if command_parts[0] not in VALID_COMMANDS:
        return "Invalid command", 400

    # Safely executing the command
    result = subprocess.run(command_parts, stdout=subprocess.PIPE)

    return result.stdout, 200


if __name__ == "__main__":
    app.run(debug=False)