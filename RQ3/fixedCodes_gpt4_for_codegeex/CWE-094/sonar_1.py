from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from the request object.
    Import the urllib module with the version.
    '''
    module_version = request.args.get('module_version')
    if not module_version:
        return "Error: module_version is required", 400
    module_version = int(module_version)
    if module_version == 2:
        import urllib2 as urllib
    elif module_version == 3:
        import urllib3 as urllib
    else:
        return "Error: Unsupported module version", 400

    return "Module version: " + str(module_version)