from flask import request, redirect, Flask, url_for
from urllib.parse import urlparse, urljoin
import os

app = Flask(__name__)

@app.route('/')
def default():
    return "This is default page"

@app.route('/flask_redirect', methods=['GET'])
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    url = request.args.get('url')
    # Validate the URL before redirecting
    if is_safe_url(url):
        return redirect(url, code=302)
    else:
        # Redirect to a default page if the URL is not valid
        return redirect(url_for('default'), code=302)

def is_safe_url(target):
    '''
    Test a URL to ensure it is safe to redirect to
    '''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

if __name__ == '__main__':
    # Use an environment variable to control whether the app is run in debug mode
    app.run(debug=os.environ.get('DEBUG', False))