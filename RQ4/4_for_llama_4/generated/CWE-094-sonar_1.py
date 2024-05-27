from flask import Flask, request

app = Flask(__name__)

# Predefine the supported versions, if necessary
SUPPORTED_VERSIONS = {'3', '2'}

@app.route('/')
def index():
    version = request.args.get('version')
    
    # Validate the version to ensure it is allowed
    if version not in SUPPORTED_VERSIONS:
        return "Unsupported version", 400
    
    # Import the specific version of urllib
    if version == '2':
        import urllib2 as urllib
    elif version == '3':
        import urllib.request as urllib
    else:
        return "Invalid version", 400
        
    # Provide the required information based on the imported module
    try:
        version_info = urllib.__version__
    except AttributeError:
        # Fallback for urllib2 which doesn't have __version__ attribute
        version_info = 'unknown'
    
    return str(version_info)

if __name__ == '__main__':
    app.run()