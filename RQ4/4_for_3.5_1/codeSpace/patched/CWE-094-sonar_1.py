from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from the request object
    importing the urllib module with the version by using exec()
    '''
    exec('import urllib')
    version = urllib.__version__
    return f"The urllib module version is: {version}"

if __name__ == "__main__":
    app.run()