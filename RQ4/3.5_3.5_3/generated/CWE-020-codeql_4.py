from flask import Flask, redirect, request, abort, url_for
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('url')  # get target URL from request
    if target_url is not None and is_valid_domain(target_url):
        return redirect(secure_url(target_url))  # redirect to target URL with secure_url
    abort(404)  # return 404 error if target URL is invalid

def secure_url(url):
    '''
    Add a prefix "https://" to the target URL to ensure a secure URL is used
    '''
    return urljoin('https://', url)

def is_valid_domain(url):
    '''
    Check if the given URL contains a valid domain
    '''
    parsed_url = urlparse(url)
    return parsed_url.netloc in valid_domains

valid_domains = ['example.com', 'example.org', 'example.net']  # list of valid domains

if __name__ == '__main__':
    app.run()