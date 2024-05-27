from flask import Flask, redirect, request, url_for
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

# Function to validate URL
def is_safe_url(target_url, host_url):
    ref_url = urlparse(host_url)
    test_url = urlparse(urljoin(host_url, target_url))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

# Function to check domain
def is_allowed_domain(url):
    allowed_domains = {"example.com"}
    domain = urlparse(url).netloc
    return any(domain == allowed_domain or domain.endswith('.' + allowed_domain)
               for allowed_domain in allowed_domains)

@app.route('/redirect')
def redirectToTarget():
    # Get the target URL from the request
    target_url = request.args.get('target_url', '')

    if not target_url:
        # No target URL provided
        return 'No target URL provided', 400

    # Make sure the target URL is relative and does not lead to any other protocol like ftp:
    if not target_url.startswith('/'):
        return 'Invalid target URL', 400

    # Create an absolute URL for safer comparison
    full_target_url = urljoin(request.host_url, target_url)

    # Ensure the target URL is within the allowed domains whitelist
    if not is_allowed_domain(full_target_url):
        return 'Invalid target URL', 400

    # Make sure redirects stay within the same domain as the host
    if not is_safe_url(target_url, request.host_url):
        return 'Unsafe redirect attempt', 400

    # Redirect to the validated target URL
    return redirect(full_target_url)

if __name__ == '__main__':
    # Specify the host to be 'localhost' for security purposes and a specific port if needed
    app.run(host='127.0.0.1', port=5000)