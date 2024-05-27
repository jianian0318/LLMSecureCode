from flask import Flask, request
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from the request object
    importing the urllib module with the version by using exec()
    '''
    version = request.args.get('version')
    exec('import urllib' + version)
    return "Module Imported"
    
if __name__ == "__main__":
    app.run(debug=True)