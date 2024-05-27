from flask import Flask, redirect, request
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

def is_valid_domain(url):
    # Parse the URL and extract the domain
    netloc = urlparse(url).netloc

    # Check if the domain is not empty and if it contains a '.' character (as a simple validity check)
    # Also check if the scheme is HTTP or HTTPS
    # This will prevent redirects to other schemes like 'data:', 'javascript:', etc.
    return netloc and '.' in netloc and (url.startswith('http://') or url.startswith('https://'))


@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('url') # Expect 'url' parameter to provide the target URL
    if target_url and is_valid_domain(target_url):
        # If the target URL is valid, use urljoin to ensure it is a relative URL and redirect to it
        safe_url = urljoin(request.host_url, target_url)

        # Ensure that the safe_url is within the same domain as the current application
        if not is_valid_domain(safe_url):
            return "Invalid URL specified", 400

        return redirect(safe_url, code=302)
    else:
        # If it is not valid, return an error response
        return "Invalid URL specified", 400

if __name__ == '__main__':
    app.run()