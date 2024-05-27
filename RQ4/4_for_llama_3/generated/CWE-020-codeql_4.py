from flask import Flask, redirect, request, url_for, abort
from urllib.parse import urlparse, urljoin
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define the list of allowed hosts for redirection
allowed_hosts = {'www.mysite.com', 'www.anothersite.com'}

# Helper function to validate URLs
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

@app.route('/redirect')
def redirectToTarget():
    # Get the target URL from the request
    target_url = request.args.get('target', None)
    
    # If the target URL is empty, redirect to home page or abort with 400 Bad Request
    if not target_url:
        abort(400)

    # Make the URL absolute by joining it to the base URL
    full_url = urljoin(request.host_url, target_url)

    # Validate the URL to ensure it's safe (i.e., same origin)
    if is_safe_url(full_url):
        # If allowed, redirect to the target URL
        return redirect(full_url)
    else:
        # If not allowed, redirect to a safe page
        return redirect(url_for('index'))

@app.route('/')
def index():
    return "Welcome to the homepage!"

if __name__ == '__main__':
    app.run()