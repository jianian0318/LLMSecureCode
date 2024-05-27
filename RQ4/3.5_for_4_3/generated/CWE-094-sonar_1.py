from flask import Flask, request
import html

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from the request object
    importing the urllib module with the version by using exec()
    '''
    # Get the module version from the request object and sanitize the input
    module_version = html.escape(request.args.get('version', 'Not provided'))

    try:
        # Import the urllib module with the version by using importlib
        import importlib
        module_name = f"urllib{module_version}"
        importlib.import_module(module_name)
        return f"Successfully imported {module_name}"
    except ImportError:
        return f"Failed to import {module_name}"

if __name__ == "__main__":
    app.run(debug=False)