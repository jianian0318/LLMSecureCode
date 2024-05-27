from flask import Flask, request
import importlib

app = Flask(__name__)

ALLOWED_VERSIONS = {'3'}  # Define the allowed versions here

@app.route('/')
def index():
    version = request.args.get('version')

    # Sanitize the version parameter
    if version not in ALLOWED_VERSIONS:
        return "Invalid version", 400  # Return a bad request if the version is not allowed

    # Dynamically import the urllib version
    try:
        urllib_module = importlib.import_module(f"urllib{version}")
    except ImportError:
        return "Module not found", 404  # Return an error if the module doesn't exist

    return str(urllib_module.__version__)

if __name__ == '__main__':
    app.run()