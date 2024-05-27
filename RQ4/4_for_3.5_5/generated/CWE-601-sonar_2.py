from flask import request, redirect, Flask, abort
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

# List of safe domains
ALLOWED_HOSTS = ['www.example.com', 'safe-site.com']

@app.route('/flask_redirect', methods=['GET'])
def flask_redirect():
    '''
    Get the URL from the request, validate it, and redirect to it if it's safe
    '''
    url = request.args.get('url')
    
    # Validate the URL before redirecting
    if url and is_url_safe(url):
        # Ensuring the redirection is to a safe, intended destination
        safe_url = urljoin(request.host_url, url)
        return redirect(safe_url)
    else:
        return abort(400, description="Bad Request: Invalid or unsafe redirect URL provided.")

def is_url_safe(url):
    '''
    Check if the URL belongs to one of the allowed hosts
    '''
    try:
        parsed_url = urlparse(url)
        # Ensures that the hostname is within our allowed hosts
        if parsed_url.hostname and parsed_url.hostname in ALLOWED_HOSTS:
            return True
        return False
    except ValueError:
        return False

if __name__ == "__main__":
    app.run(debug=False)  # Disable debug for production deployment