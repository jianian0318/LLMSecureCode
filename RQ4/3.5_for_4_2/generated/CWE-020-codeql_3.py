from flask import Flask, redirect, request, url_for
import re
import urllib.parse

app = Flask(__name__)

# Regular expression pattern to match valid URLs
# (simple version for demonstration purposes)
pattern = re.compile(r'^(http[s]?://)?[a-z0-9\-]+(\.[a-z0-9\-]+)+(/[^/]+)*/?$')

@app.route('/redirect')
def redirectToTarget():
    # Get target URL from query parameters
    target = request.args.get('target', None)

    # If target is not provided or does not pass the validity check,
    # redirect to the root path by default
    if target is None or not pattern.match(target):
        return redirect(url_for('root'))

    # Sanitize the target URL to prevent URL redirection attacks
    sanitized_target = urllib.parse.quote(target, safe='')
   
    # Validate the target URL for redirection
    if is_safe_redirect(sanitized_target):
        # If everything is okay, redirect to the target URL
        return redirect(sanitized_target, code=302)
    else:
        # If the target URL is not safe, redirect to a safe default URL
        return redirect(url_for('safe'))

def is_safe_redirect(url):
    # Validate that the target URL is safe for redirection
    # Add your custom logic here to determine whether the URL is safe or not
    # You can use external libraries or services for this validation
    # For the demonstration purposes, let's assume all URLs are safe
    return True

@app.route('/')
def root():
    return "Welcome to the root page!"

@app.route('/safe')
def safe():
    return "Redirecting to a safe default URL"


if __name__ == '__main__':
    app.run()