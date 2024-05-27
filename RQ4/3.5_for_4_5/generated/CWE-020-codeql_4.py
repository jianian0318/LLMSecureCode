from flask import Flask, redirect, request, abort
from urllib.parse import urlparse, urljoin

def isValidURL(url):
    '''
    This function checks if a URL contains a valid domain.
    It returns True if the domain is valid, False otherwise.
    '''
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request args with 'url' as key, check if it contains 
    a valid domain using isValidURL function, and then redirect to the target URL,
    otherwise return an error message.
    '''
    url = request.args.get('url')
    if url is not None:
        if isValidURL(url):
            parsed_url = urlparse(url)
            if parsed_url.scheme not in ['http', 'https']:
                abort(400, 'Invalid URL scheme, only http and https are allowed')
            elif 'example.com' in parsed_url.netloc:
                abort(400, 'Invalid target URL')
            else:
                safe_url = urljoin(request.base_url, url)
                return redirect(safe_url)
        else:
            abort(400, 'Invalid URL provided')
    else:
        abort(400, 'No URL provided')

if __name__ == '__main__':
    app.run()