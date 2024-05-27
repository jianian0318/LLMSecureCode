from flask import Flask, request, escape

app = Flask(__name__)

# Define a whitelist of allowed module versions
ALLOWED_VERSIONS = ['3', '3.5']

@app.route('/')
def index():
    # Get the module version and escape it to prevent XSS
    module_version = escape(request.args.get('module_version', ''))
    
    # Only import allowed versions
    if module_version in ALLOWED_VERSIONS:
        # Importing the module safely assuming the whitelist contains only safe versions
        module = __import__(f"urllib{module_version}")
        return f"Module version: {module_version}"
    else:
        return "Invalid module version!"

if __name__ == '__main__':
    app.run()