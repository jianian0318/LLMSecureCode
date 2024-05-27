from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from the request object
    importing the urllib module with the version by using eval()
    '''
    module_version = request.headers.get('X-Module-Version', '')
    
    module_name = f'urllib{module_version}'
    try:
        urllib = eval(module_name)
    except ModuleNotFoundError:
        return 'Invalid module version'
    
    return 'Hello, World!'