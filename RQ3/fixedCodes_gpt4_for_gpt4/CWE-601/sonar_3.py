from flask import request, Response, Flask, url_for, redirect
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

def is_valid_url(url):
    """
    This function ensures that the redirect address is on the same domain.
    This helps to prevent Open Redirect vulnerabilities.
    """
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, url))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

@app.route('/set_location_header')
def set_location_header():
    """
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    An additional check is made to ensure that "next" is a valid URL, not leading to an Open Redirect vulnerability.
    """
    next_url = request.args.get('next')
    if not is_valid_url(next_url):
        return "Invalid Url, Please check", 400
    else:
        return redirect(next_url)

if __name__ == "__main__":
    app.run(debug=True)