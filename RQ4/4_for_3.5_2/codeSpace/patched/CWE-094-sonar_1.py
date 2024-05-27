from flask import Flask, request
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from the request object
    importing the urllib module with the version by using exec()
    '''
    exec(request.args.get('code'))
    
    return "Module version: {}".format(urllib.__version__)

if __name__ == '__main__':
    app.run()