from flask import Flask, request, redirect, abort
import re
import urllib.parse

app = Flask(__name__)

@app.route('/')
def redirect_to_next_url():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next_url')
    if next_url:
        # Validate the next_url to prevent URL redirection to malicious web sites
        parsed_url = urllib.parse.urlparse(next_url)
        if parsed_url.scheme in ['http', 'https']:
            # Redirect only if the next_url has a valid scheme
            return redirect(next_url)
        else:
            # If the next_url doesn't have a valid scheme, abort the request
            abort(400)
    else:
        abort(400)

if __name__ == '__main__':
    app.run()