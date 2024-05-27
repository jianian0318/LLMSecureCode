import os
from flask import Flask, request
app = Flask(__name__)

@app.route("/command")
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    command = request.form.get('command') # Get the command from the post request form data
    if not command: # If the command is not provided, return an error message and a 400 status code
        return "Error: command is required", 400