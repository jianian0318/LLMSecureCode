import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/command", methods=["POST"]) 
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    command = request.form.get('command')

    # Validation could be anything depending upon the scenario.
    # But for now, it just confirms the command is not none.
    if command:
        os.system(command)
        return "Command executed."
    else:
        return "Invalid command"

if __name__ == "__main__":
    app.run(debug=True)