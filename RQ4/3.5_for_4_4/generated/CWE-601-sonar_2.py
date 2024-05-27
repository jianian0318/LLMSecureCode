from flask import request, redirect, Flask, abort
import validators

app = Flask(__name__)

@app.route('/flask_redirect', methods=['GET'])
def flask_redirect():
    '''
    Get the url from request args and redirect to it
    '''
    url = request.args.get('url')

    # Validate the URL to prevent redirecting to malicious websites
    if url:
        # Use the validators library to validate the URL
        if not validators.url(url):
            # Malformed URL, abort the request
            abort(400)
    else:
        # Redirect to a default page if no URL is provided
        url = 'https://example.com'

    # Ensure that the URL is properly encoded to prevent any injection attacks
    encoded_url = redirect(url, code=302).location

    # Use the redirect() function to perform the redirection
    return redirect(encoded_url, code=302)