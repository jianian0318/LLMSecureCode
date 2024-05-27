from flask import Flask, request
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from the request object
    importing the urllib module with the version by using exec()
    '''
    version = None
    if request.args.get('version'):
        version = request.args.get('version')
        try:
            exec('import urllib' + version)  # Import urllib module with the specified version
            urllib_version = eval('urllib.__version__')  # Get the actual version of urllib module
            return f'The version of urllib module is {urllib_version}'
        except ImportError:
            return f'Invalid urllib version'
    else:
        return f'Module version is not provided'

if __name__ == "__main__":
    app.run()