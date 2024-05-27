from flask import Flask, redirect, request, abort, Markup
import urllib.parse
import validators

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    # Get target URL from the request
    target_url = request.args.get('target')

    if not target_url:
        return 'Invalid request', 400

    if not validators.url(target_url):
        return 'Invalid URL', 400

    # Validate target URL and redirect the user if it's valid
    if is_valid_url(target_url):
        return redirect(target_url)
    else:
        return 'Invalid URL', 400

def is_valid_url(url):
    allowed_schemes = ['http', 'https']
    for scheme in allowed_schemes:
        if url.startswith(scheme):
            return True
    return False

if __name__ == "__main__":
    app.run()