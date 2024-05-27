from flask import Flask
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    """
    This route displays the version of urllib module.
    """
    version = urllib.__version__
    return f"The version of urllib module is: {version}"