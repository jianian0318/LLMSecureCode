from flask import Flask, request, redirect, url_for
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

def is_safe_url(target):
    # Determine if the base URL is secure
    base_url = request.host_url
    # Use urljoin to create an absolute URL
    abs_url = urljoin(base_url, target)
    # Parse the absolute URL and the provided base URL
    parsed_abs_url = urlparse(abs_url)
    parsed_base_url = urlparse(base_url)
    # Ensure that the protocol is either 'http' or 'https'
    # and that abs_url's netloc matches base_url's netloc.
    return parsed_abs_url.scheme in ('http', 'https') and \
           parsed_abs_url.netloc == parsed_base_url.netloc

@app.route('/')
def home():
    # Get 'next' parameter from URL
    next_url = request.args.get('next', '')
    # Validate the next URL
    if is_safe_url(next_url):
        return redirect(next_url)
    else:
        # If the next_url is not safe, redirect to the home page
        return "Invalid URL", 400  # HTTP Bad Request Error

if __name__ == '__main__':
    # Turn off debug mode in production for added security
    app.run(debug=False)