import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    command = request.form['command']
    if command in ['ls', 'pwd', 'whoami']:
        output = os.popen(command).read()
        return output
    else:
        return "Invalid command"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
