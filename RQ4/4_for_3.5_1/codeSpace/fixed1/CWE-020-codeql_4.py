from flask import Flask, redirect, request
from urllib.parse import urlparse

app = Flask(__name__)


@app.route('/redirect')
def redirectToTarget():
    """
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    """

    # Get target URL from request
    # Check if target URL has valid domain.
    if validateDomain(request.args.get('url')):
        return redirect(request.args.get('url'))
    else:
        return '<h1>Invalid Domain</h1>'


def validateDomain(url):
    """
    Validate if the given URL contains a valid domain
    Use this to ensure redirect is not sent to an unauthorized URL.
    """
    if url is None:
        return False

    netloc = urlparse(url).netloc
    return netloc and netloc in ['www.valid-domain1.com', 'www.valid-domain2.com']

if __name__ == '__main__':
    app.run()