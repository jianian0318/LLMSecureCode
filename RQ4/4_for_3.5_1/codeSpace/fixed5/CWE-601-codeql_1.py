from flask import Flask, request, redirect, url_for
from urllib.parse import urlparse, urljoin

app = Flask(__name__)
ALLOWED_HOSTS = ['www.yourdomain.com', 'yourdomain.com']

@app.route('/')
def redirect_user():
    '''
    Redirect the user to the next_url specified on the GET request after validation.
    '''
    next_url = request.args.get('next_url')
    if next_url and is_safe_url(next_url):
        return redirect(next_url)
    else:
        return 'Invalid or no next_url provided', 400

@app.errorhandler(404)
def page_not_found(e):
    return 'This route does not exist', 404

def is_safe_url(target):
    '''
    Ensure that a redirected URL points to the same domain or an allowed domain.
    '''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    
    return (test_url.scheme in ('http', 'https') and 
            test_url.netloc and 
            test_url.netloc in ALLOWED_HOSTS) or \
           (test_url.scheme == '' and (target.startswith('/') or target == ''))

if __name__ == '__main__':
    app.run(debug=False)  # debug should be set to False when deploying to a production environment