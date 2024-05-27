from flask import Flask, redirect, request
import re
import urllib.parse

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request,
    use a regular expression to check if it is a valid target,
    then redirect to the target URL
    '''
    # Get the target URL from the request arguments
    target_url = request.args.get('url')

    # Validate target URL
    if is_valid_url(target_url):
        real_target_url = urllib.parse.urlparse(target_url)
        if real_target_url.scheme and real_target_url.netloc:
            # Check if the scheme and netloc are present
            return redirect(real_target_url.geturl())
        else:
            return 'Invalid URL', 400
    else:
        return 'Invalid URL', 400

def is_valid_url(url):
    '''
    Check if the provided URL is a valid target
    '''
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc])
    except (ValueError, AttributeError):
        return False

if __name__ == "__main__":
    app.run(debug=False)