from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from the request object
    '''
    import urllib
    version = urllib.__version__
    # return version
    return f"urllib version: {version}"

if __name__ == "__main__":
    app.run()