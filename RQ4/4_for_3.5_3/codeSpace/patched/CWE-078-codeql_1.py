import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/command", methods=["POST"])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    command = request.form.get("command")
    if command is None:
        return "Invalid command", 400
    
    try:
        result = os.system(command)
        return str(result)
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run()