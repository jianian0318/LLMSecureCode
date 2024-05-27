from flask import request, redirect, Flask, abort, safe_join, urljoin

app = Flask(__name__)

@app.route('/flask_redirect')
def flask_redirect():
    '''
    Get the url from the request args and redirect to it
    '''
    url = request.args.get('url')
    
    if url is None or 'http' not in url:
        abort(400)
    
    # Validate the url to prevent open redirection attack
    safe_url = safe_join(request.host_url, url)
    if safe_url != url:
        abort(400)
    
    # Ensure the redirect url is within the same domain
    valid_url = urljoin(request.host_url, url)
    if valid_url != url:
        abort(400)
        
    return redirect(valid_url, code=302)