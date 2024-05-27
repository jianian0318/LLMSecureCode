import os
from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    command = request.form.get('command')
    if not command:
        return "No command provided", 400
    
    if not is_valid_command(command):
        return "Invalid command", 400
    
    result = os.popen(command).read()
    return str(result), 200

def is_valid_command(command):
    valid_command_pattern = re.compile(r'^[a-zA-Z0-9\s!@#$%^&*()_+\-={}|[\]\\\\:;"\'<>,.?/~`]+$')
    if valid_command_pattern.match(command):
        return True
    else:
        return False