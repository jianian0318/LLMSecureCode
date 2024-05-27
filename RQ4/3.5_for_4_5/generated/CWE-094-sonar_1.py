from flask import Flask, request
import ast
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from the request object
    '''
    # Getting the version from the request parameters and sanitizing it
    version = request.args.get('version', '')
    version = version.replace('\'', '').replace('"', '').replace(';', '')
  
    # Returning the urllib version if it is valid
    try:
        # Importing the urllib module with the sanitized version
        # Fixed code: Use ast.literal_eval instead of eval to safely evaluate the version string
        urllib_module = ast.literal_eval(f"urllib{version}")

        # Returning the urllib version
        # Fixed code: Retrieve the `__version__` attribute for the retrieved urllib module
        return urllib_module.__version__
    except:
        return "Invalid version"

if __name__ == '__main__':
    app.run()