from flask import request, redirect, Flask
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/flask_redirect')
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    url = request.args.get('url')
    if url is not None:
        # Validate the url before redirection to prevent CWE-601
        
        # Check if the url starts with 'http://' or 'https://'
        if url.startswith('http://') or url.startswith('https://'):
            # Parse the url to obtain the hostname
            parsed_url = urlparse(url)
            
            # Redirect only to a trusted domain to prevent CWE-601
            if parsed_url.netloc == 'example.com':
                return redirect(url, code=302)
            else:
                return "Invalid url provided"
        else:
            return "Invalid url provided"
    else:
        return "No url provided for redirection"

if __name__ == "__main__":
    app.run()