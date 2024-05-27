from flask import Flask, redirect, request
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    # Get target url from request parameters
    target_url = request.args.get('target')

    # Check if the url is valid
    if target_url:
        parsed_url = urlparse(target_url)
        # Ensure the URL contains a valid domain
        if parsed_url.netloc:
            # Check if the URL is safe and not a malicious website
            if is_url_safe(target_url):
                return redirect(urljoin(request.url_root, target_url))
            else:
                return "Unsafe URL", 400
        else:
            return "Invalid URL", 400
    else:
        return "Bad Request", 400

def is_url_safe(url):
    '''
    Check if the URL is safe and does not point to a malicious website
    '''
    # Add any necessary checks to ensure the URL is safe
    # For example, you can check for known malicious domains, validate HTTPS, etc.
    safe_domains = ['example.com', 'example.org']
    parsed_url = urlparse(url)

    if parsed_url.netloc in safe_domains:
        return True
    else:
        return False