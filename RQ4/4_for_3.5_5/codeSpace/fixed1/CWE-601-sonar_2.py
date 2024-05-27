from flask import request, redirect, Flask, abort

app = Flask(__name__)

# List of safe domains
ALLOWED_HOSTS = ['www.example.com', 'safe-site.com']

@app.route('/flask_redirect', methods=['GET'])
def flask_redirect():
    '''
    Get the URL from the request, validate it, and redirect to it if it's safe
    '''
    url = request.args.get('url')
    
    # Only redirect to allowed hosts
    if url and is_url_safe(url):
        return redirect(url)
    else:
        return abort(400, description="Bad Request: Invalid or unsafe redirect URL provided.")

def is_url_safe(url):
    '''
    Check if the URL belongs to one of the allowed hosts
    '''
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    
    if parsed_url.hostname in ALLOWED_HOSTS:
        return True
    return False

if __name__ == "__main__":
    app.run()