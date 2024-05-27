from flask import Flask, request, redirect, url_for

app = Flask(__name__)

ALLOWED_HOSTS = ['www.yourdomain.com', 'yourdomain.com', 'localhost', '127.0.0.1']

@app.route('/')
def redirect_user():
    '''
    Redirect the user to the next_url specified on the GET request after validation.
    '''
    next_url = request.args.get('next_url')
    if next_url:
        # Validate the next_url
        if is_safe_url(next_url):
            return redirect(next_url)
        else:
            return 'Invalid redirection URL', 400
    else:
        return 'No next_url provided'


@app.errorhandler(404)
def page_not_found(e):
    return 'This route does not exist', 404

def is_safe_url(target):
    # Use urlparse to parse the URL and check if the host is in ALLOWED_HOSTS
    from urllib.parse import urlparse, urljoin
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    # Validate if the target URL is the same domain or a relative URL
    if test_url.scheme in ('http', 'https') and \
       test_url.netloc and \
       test_url.netloc not in ALLOWED_HOSTS:
        return False
    # Also consider that the target is on the same domain or a subdomain, and the target path is valid
    return test_url.scheme in ('', 'http', 'https') and \
           (test_url.netloc == ref_url.netloc or test_url.netloc.endswith('.' + ref_url.netloc))

if __name__ == '__main__':
    app.run(debug=False)  # debug should be set to False when deploying to a production environment