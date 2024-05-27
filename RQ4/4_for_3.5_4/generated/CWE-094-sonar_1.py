from flask import Flask
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Attempt to get the version of the urllib module directly.
    '''
    try:
        # Import the version info directly from urllib
        version = urllib.__version__
    except AttributeError:
        # Handling the case where __version__ is not found
        version = "Version attribute not found in urllib module"
    
    return f"Urllib version: {version}"

if __name__ == '__main__':
    app.run()