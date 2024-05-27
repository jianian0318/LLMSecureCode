from flask import request, Response, Flask, redirect, url_for
from urllib.parse import urlparse, urljoin
app = Flask(__name__)

@app.route('/set_location_header', methods=['GET'])
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    next_url = request.args.get('next')
    if next_url:
        # Ensures the redirect URL is safe to redirect to.
        if is_safe_url(next_url):
            return redirect(next_url)
    return Response(status=400)

def is_safe_url(target):
    # Ensure the redirect URL is within the same domain
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return ref_url.netloc == test_url.netloc