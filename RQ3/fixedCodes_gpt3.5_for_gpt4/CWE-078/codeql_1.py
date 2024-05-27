import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    data = request.get_json()

    if 'command' not in data:
        return jsonify({'error': 'No command provided'}), 400

    command = data['command']

    output = subprocess.getoutput(command)

    return jsonify({'output': output}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)