from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from the request object
    importing the urllib module with the version by using exec()
    '''
    module_version = request.args.get('module_version') # Get the module version from the request object
    if not module_version: # If the module version is not provided, return an error message and a 400 status code
        return "Error: module_version is required", 400
    exec(f'import urllib{module_version}') # Import the urllib module with the version by using exec()

    return "Module version: " + module_version