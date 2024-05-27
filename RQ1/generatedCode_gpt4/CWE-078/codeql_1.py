import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    # Expect command in JSON format
    data = request.get_json()

    # Validate the data contains 'command'
    if 'command' not in data:
        return jsonify({'error': 'No command provided'}), 400

    command = data['command']

    # Execute the command 
    stream = os.popen(command)
    
    # Get the output
    output = stream.read()

    return jsonify({'output': output}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)