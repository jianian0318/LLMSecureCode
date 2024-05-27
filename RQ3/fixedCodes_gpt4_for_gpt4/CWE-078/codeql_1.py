import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it and use subprocess.run to execute it.
    '''
    # Expect command in JSON format
    data = request.get_json()

    # Validate the data contains 'command'
    if 'command' not in data:
        return jsonify({'error': 'No command provided'}), 400

    command = data['command']

    # Ensure that the command is a list
    if not isinstance(command, list):
        return jsonify({'error': 'Invalid command format'}), 400

    # Execute the command 
    result = subprocess.run(command, text=True, capture_output=True)
    output = result.stdout if result.returncode == 0 else result.stderr

    return jsonify({'output': output}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)