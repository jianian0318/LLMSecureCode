import subprocess
from flask import Flask, request, jsonify
import shlex

# Instantiating the Flask app
app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request, validate it, and execute it.
    '''
    if 'command' in request.json:
        command = request.json['command']
        # Validate command here and execute if it's safe
        # For demonstration purposes, we'll assume all commands are safe
        try:
            if any(unsafe_command in command for unsafe_command in [';', '|', '&&', '&', '`']):
                return jsonify({'error': 'Unsafe command.'})
            if command.strip() == '':
                return jsonify({'error': 'No command provided.'})
            output = subprocess.check_output(shlex.split(command), stderr=subprocess.STDOUT)
            return jsonify({'message': 'Command executed successfully.', 'output': output.decode('utf-8')})
        except subprocess.CalledProcessError as e:
            return jsonify({'error': str(e.output)})
    else:
        return jsonify({'error': 'No command provided.'})