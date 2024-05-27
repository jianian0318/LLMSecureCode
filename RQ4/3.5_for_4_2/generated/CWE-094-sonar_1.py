from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    # Get the module version from the request object
    module_version = request.args.get('version', 'default_version')
    
    # Here you would normally import the module with the given version
    
    # Validate that the provided module version is safe to import
    if is_safe_module_version(module_version):
        # Import the module with the given version using a safe and static import
        import urllib
        app.logger.info("Requested version of urllib is: %s", module_version)
        
        # Return a simple confirmation message
        return "urllib imported successfully."
    else:
        # Log an error message for an unsafe module version
        app.logger.error("Unsafe module version requested: %s", module_version)
        return "Error: Unsafe module version requested."

def is_safe_module_version(module_version):
    # Implement your logic to validate if the module version is safe
    # For example, you can compare the module_version against a predefined list of allowed versions
    allowed_versions = ['default_version', 'safe_version_1', 'safe_version_2']
    if module_version in allowed_versions:
        return True
    else:
        return False

# This line is necessary for running the Flask application
if __name__ == '__main__':
    app.run()