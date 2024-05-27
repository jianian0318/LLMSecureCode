from flask import request, redirect, Flask, url_for, abort
from urllib.parse import urlparse, urljoin
app = Flask(__name__)

def is_safe_url(target):
    """
    Checks if the target URL is safe for redirection.
    """
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

@app.route('/flask_redirect')
def flask_redirect():
    '''
    Get the url from the request, validate it, and redirect to it
    '''
    url = request.args.get('url')  # Get the url parameter from the request
    if url and is_safe_url(url):  # Validate the url
        return redirect(url)  # redirect to the url
    else:
        return abort(400, 'Bad Request: the redirection was blocked for security reasons.')

if __name__ == "__main__":
    app.run(debug=False)