from flask import Flask, redirect, request
import re
import urllib.parse

app = Flask(__name__)

def is_valid_url(url):
    '''
    Checks if the given URL is valid or not
    '''
    # Verify if the url is valid.
    # This is a very basic check, and real-world applications should do a more exhaustive check.
    if re.match(r'^http(s)?://[a-zA-Z0-9\.-]+\.[a-zA-Z]{2,7}(/\S*)?$', url):
        return True
    else:
        return False

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('target_url', None)
    if target_url:
        if is_valid_url(target_url):
            parsed_url = urllib.parse.urlparse(target_url)
            if parsed_url.scheme and parsed_url.netloc:
                return redirect(target_url, code=302)
            else:
                return ("Invalid URL format", 400)
        else:
            return ("Invalid URL format", 400)
    else:
        return ('No target URL provided', 400)