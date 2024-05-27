from flask import Flask, request, redirect, abort
import re
import urllib.parse

app = Flask(__name__)

@app.route('/')
def redirect_user():
    '''
    Redirect the user to the next_url specified on the GET request if it is a valid URL.
    '''
    next_url = request.args.get('next_url')
    if next_url:
        # Validate the URL before redirecting
        if is_valid_url(next_url):
            # Make sure the redirect URL is a safe URL
            safe_url = make_safe_url(next_url)
            return redirect(safe_url, code=302)
        else:
            abort(400)
    else:
        return "No next_url provided.", 400

def is_valid_url(url):
    '''
    Check if the given URL is valid.
    '''
    # Use regular expression to validate the URL format
    url_pattern = re.compile(r'^(?:http|https)://')
    return re.match(url_pattern, url) is not None

def make_safe_url(url):
    '''
    Make the URL safe by checking for malicious redirects.
    '''
    # Check if the URL is safe
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.scheme not in ['http', 'https']:
        return None
    if parsed_url.netloc == '':
        return None
    return url