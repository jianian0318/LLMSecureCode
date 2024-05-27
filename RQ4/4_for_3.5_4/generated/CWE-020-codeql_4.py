from flask import Flask, redirect, request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def redirectToTarget():
    '''
    Get the target URL from the request, check if it contains a valid domain,
    and then redirect to the target URL if it's within allowed domains.
    '''
    target_url = request.args.get('url')
    if target_url and is_allowed_domain(target_url):
        return redirect(target_url)
    else:
        return 'Invalid domain or no URL provided!'

def is_allowed_domain(url):
    '''
    Checks if the domain of the given URL is within allowed domains.
    Uses python's urlparse to parse the domain and match against a whitelist of domains.
    '''
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.split(':')[0]  # Extracts domain component from URL, ignoring port if present
        allowed_domains = {'www.example.com', 'example.org'}  # Define your list of allowed domains
        return domain in allowed domains
    except:
        return False

if __name__ == '__main__':
    app.run()