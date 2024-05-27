from flask import Flask, request, redirect, url_for
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

@app.route('/')
def redirect_url():
    '''
    Redirects the user to the next_url specified on the GET request after validating it.
    '''
    next_url = request.args.get('next_url')
    if next_url:
        # Checks if the url is safe
        if is_safe_url(next_url):
            return redirect(next_url)
        else:
            return "Unsafe next URL parameter provided"
    else:
        return "No next URL parameter provided"


# A function to ensure safe redirecting
def is_safe_url(target):
    '''
    Checks if a URL is safe for redirects.
    '''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


if __name__ == "__main__":
    app.run(debug=False)