import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    command = request.form.get('command')
    if not command:
        return "No command provided", 400
    
    # validate the command
    if not is_valid_command(command):
        return "Invalid command", 400
    
    # execute the command
    result = os.system(command)
    
    # return the result
    return str(result), 200

def is_valid_command(command):
    # add your command validation logic here
    return True