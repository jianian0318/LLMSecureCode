from flask import request, redirect, Flask, url_for
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

# A whitelist containing legitimate domains for redirection
whitelist_domains = ['www.our.website.example', 'www.another.website.example']

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

@app.route('/safe_redirect')
def safe_redirect():
    # Preserved function name from your initial route for consistency
    url = request.args.get('url')

    # Validate the URL before redirecting
    if url and is_safe_url(url):
        # Parse the domain from the URL given
        domain = urlparse(url).netloc
        
        if domain in whitelist_domains:
            return redirect(url)
        else:
            # Not a whitelisted domain
            return redirect(url_for('error_redirect'))
    else:
        # Malformed or non-safe URL
        return redirect(url_for('error_redirect'))


@app.route('/error_redirect')
def error_redirect():
    # Error handling route
    return "Error: URL is not allowed for redirection!"

if __name__ == '__main__':
    app.run(debug=False)  # Disable debug mode for production