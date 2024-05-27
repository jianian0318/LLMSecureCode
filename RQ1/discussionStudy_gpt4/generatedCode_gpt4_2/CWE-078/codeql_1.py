import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request,
    validate it, and execute it.
    '''
    command = request.form['command']  # Get command from POST request body
    if command:
        return os.popen(command).read() # Execute the command & return the result
    else:
        return 'No command received'

if __name__ == "__main__":
    app.run()