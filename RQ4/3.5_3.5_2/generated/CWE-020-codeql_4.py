from flask import Flask, redirect, request
import urllib.parse

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('target')

    # Check if target URL contains a valid domain
    parsed_url = urllib.parse.urlparse(target_url)
    if parsed_url.netloc == 'example.com':
        return redirect(parsed_url.geturl())
    else:
        return 'Invalid URL'