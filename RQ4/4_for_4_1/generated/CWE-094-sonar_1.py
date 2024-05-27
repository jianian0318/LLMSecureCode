from flask import Flask, request

app = Flask(__name__)

urllib_versions = {
    '2': __import__('urllib2'),
    '3': __import__('urllib3'),
}

@app.route('/')
def index():
    # Extract `module_version` from query parameters
    module_version = request.args.get('version', 'No version specified')

    # Safely import `urllib` based on the version number
    urllib_module = urllib_versions.get(module_version, None)
    
    if urllib_module:
        version_info = "Module imported successfully"
    else:
        version_info = f"An error occurred while importing: Version {module_version} is not available or not supported."

    return version_info

if __name__ == "__main__":
    app.run(debug=False)