from flask import request, Response, Flask, url_for
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

@app.route('/set_location_header')
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    next_url = request.args.get('next')
    if next_url:
        # Secure the redirection by ensuring the redirection URL is a local URL
        if is_safe_url(next_url):
            return Response(status=302, headers={'Location': next_url})
        else:
            return 'Invalid or unsafe "next" value provided.'
    else:
        return 'No "next" value provided.'

def is_safe_url(target):
    '''
    Check if the URL is a safe URL (internal)
    '''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc