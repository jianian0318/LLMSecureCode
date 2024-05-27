from flask import Flask, redirect, request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/redirect', methods=['POST'])
def redirectToTarget():
    '''
    Get target URL from request, validate its domain, and 
    then redirect to the target URL if it is valid.
    Otherwise, return an error message.
    '''
    target_url = request.form.get('url')
    if target_url and valid_domain(target_url):
        return redirect(target_url)
    else:
        return 'Invalid domain or missing URL', 400

def valid_domain(url):
    '''
    Validate domains using urlparse to ensure redirection is to approved hostnames only.
    '''
    # Parse the URL
    parsed_url = urlparse(url)
    # Check if the scheme is http or https and if the domain is from a trusted source
    return parsed_url.scheme in {'http', 'https'} and parsed_url.netloc.endswith(('yoursite.com', 'trustedsource.com'))

if __name__ == '__main__':
    app.run(debug=False)