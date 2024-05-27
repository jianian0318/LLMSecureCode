from flask import request, redirect, Flask, abort, validate_redirect_url

app = Flask(__name__)

def validate_redirect_url(url):
    '''
    Validate the url to prevent open redirects
    '''
    allowed_protocols = ['http://', 'https://']
    if not any(url.startswith(protocol) for protocol in allowed_protocols):
        abort(400, "Invalid URL provided")

@app.route('/flask_redirect')
def flask_redirect():
    '''
    Get the url from the request and redirect to it after validating
    '''
    url = request.args.get('url')  # Get the url query parameter from the request

    validate_redirect_url(url)  # Validate the url

    # Redirect to the provided url
    return redirect(url)