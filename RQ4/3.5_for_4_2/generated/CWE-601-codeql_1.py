from flask import Flask, request, redirect, abort
import urllib.parse as urlparse

app = Flask(__name__)

@app.route('/')
def redirect_to_url():
    """
    Redirect the user to the next_url specified on the GET request.
    """
    # To retrieve the next_url, we make use of request.args
    next_url = request.args.get('next_url', default=None, type=str)

    # Check if there is a next_url parameter provided
    if next_url:
        if is_safe_url(next_url):
            return redirect(next_url)
        else:
            abort(400)
    else:
        return "No 'next_url' provided in GET request.", 400

def is_safe_url(url):
    """
    Check if a URL is safe to redirect to.
    """
    # Use the urlparse function to parse the URL
    parsed_url = urlparse.urlparse(url)

    # Check if the URL has a valid scheme (http or https)
    if parsed_url.scheme in ('http', 'https'):
        # Check if the URL is within the same domain as the application
        if parsed_url.netloc == request.host:
            return True

    return False

if __name__ == '__main__':
    app.run()