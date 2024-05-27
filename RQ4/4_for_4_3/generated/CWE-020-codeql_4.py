from flask import Flask, redirect, request, escape
from urllib.parse import urlparse

app = Flask(__name__)

SAFE_URLS = [
    'example1.com',
    'example2.com',
    # add other domains here that are safe for redirect
]

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to target URL
    '''
    target = request.args.get('url')  # Get the 'url' parameter from the request
    if target is None:
        return 'No target URL provided', 400
    
    # parse the URL and check if it has a netloc part
    url_parsed = urlparse(target)
    if not url_parsed.netloc:
        return f'Invalid target URL: {escape(target)}', 400

    # check if netloc is in the SAFE_URLS list
    if url_parsed.netloc in SAFE_URLS:
        # target is in the SAFE_URLS list, redirect to it
        return redirect(target)
    else:
        return f'Invalid target URL: {escape(target)}', 400