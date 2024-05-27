from flask import Flask, request
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from urllib and return it.
    '''
    module_version = urllib.__version__
    return f'urllib version: {module_version}'
    
if __name__=="__main__":
    app.run(debug=True)