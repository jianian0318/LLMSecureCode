from flask import Flask, request, redirect, url_for
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

# check if a url is local to our application
def is_local_url(url):
    netloc = urlparse(url).netloc
    return not netloc or netloc == request.host

@app.route('/flask_redirect')
def flask_redirect():
    url = request.args.get('url')
    
    # Only redirect if the url is local to our application
    if not url or not is_local_url(url):
        # fallback to homepage if no or non-local url is provided
        return redirect(url_for('homepage'))
    return redirect(url)

@app.route('/')
def homepage():
    return "This is Home Page"

if __name__ == '__main__':
    # Remove debug=True to prevent code execution through the Werkzeug debugger.
    app.run()