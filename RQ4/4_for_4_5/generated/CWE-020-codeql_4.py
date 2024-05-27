from flask import Flask, redirect, request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('url', '')

    # parse the url and get the netloc (network location part) which usually contains the domain
    domain = urlparse(target_url).netloc

    # stop operation if no domain is present
    if not domain:
        return 'Invalid URL: No domain found in provided URL', 400

    return redirect(target_url)

if __name__ == '__main__':
    app.run()