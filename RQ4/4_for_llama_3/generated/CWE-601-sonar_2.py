from flask import request, redirect, Flask
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

def is_valid_url(url):
    """
    Function to check if the url is safe for redirection
    """
    # Takes the base URLs (having scheme, netloc and path)
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, url))
    # Validate the scheme and netloc of the redirection URL
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

@app.route('/flask_redirect')
def flask_redirect():
    url = request.args.get('url')
    # Check if the url is safe for redirection
    if not url or not is_valid_url(url):
        return "Bad Request!", 400
    return redirect(url)

if __name__ == '__main__':
    # Run the app in production mode
    app.run(debug=False)