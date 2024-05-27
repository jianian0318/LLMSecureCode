from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from the request object
    importing the urllib module with the version by using exec()
    '''
    module_version = request.headers.get('X-Module-Version', '')

    exec(f'import urllib{module_version} as urllib')

    return 'Hello, World!'