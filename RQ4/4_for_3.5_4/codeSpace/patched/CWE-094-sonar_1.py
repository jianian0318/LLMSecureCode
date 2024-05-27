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
    
    try:
        exec("import urllib.version as version")
        version = version.version
    
    except ImportError:
        version = "Module urllib not found"
    
    return f"Urllib version: {version}"

if __name__ == '__main__':
    app.run()