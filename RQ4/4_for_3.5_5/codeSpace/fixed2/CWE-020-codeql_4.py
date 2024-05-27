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
        return 'Invalid domain or missing URL'

def valid_domain(url):
    # An improved method to validate domains using urlparse and checking presence of netloc
    parsed_url = urlparse(url)
    return parsed_url.scheme in {'http', 'https'} and parsed_url.netloc.endswith(('yoursite.com', 'trustedsource.com'))

if __name__ == '__main__':
    app.run(debug=False)