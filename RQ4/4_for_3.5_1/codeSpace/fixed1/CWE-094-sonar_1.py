from flask import Flask
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Get the module version from the urllib module
    '''
    version = urllib.__version__
    return f"The urllib module version is: {version}"

if __name__ == "__main__":
    app.run()