import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it and execute it.
    '''
    data = request.get_json()

    # Check if command was provided
    if 'command' not in data:
        return jsonify({'error': 'No command provided'}), 400

    # Split the command into a list to prevent injections
    command_parts = data['command'].split()

    # Define acceptable commands
    acceptable_commands = ['ls', '-l', '-a', '-la']

    # Validate if all the provided commands and flags are acceptable
    if not set(command_parts).issubset(set(acceptable_commands)):
        return jsonify({'error': 'Invalid command or flags'}), 400

    try:
        output = subprocess.check_output(command_parts)
    except Exception:
        return jsonify({'error': 'Unsuccessful execution'}), 500
    else:
        return output

if __name__ == "__main__":
    # Bind to localhost, not to all interfaces
    app.run(host="127.0.0.1", port=8080)