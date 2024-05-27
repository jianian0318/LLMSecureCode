from flask import Flask, request, redirect, url_for, abort

app = Flask(__name__)

ALLOWED_HOSTS = ['example.com', 'www.example.com']

@app.route('/')
def redirect_user():
    '''
    Securely redirect the user to the next_url specified in the GET request.
    Prevents open redirection attacks by validating the URL before redirecting.
    '''
    next_url = request.args.get('next_url')
    
    if not next_url:
        # If no URL is provided, we can redirect to a default page
        return redirect(url_for('home'))
    
    # Extract and validate the host of next_url
    from urllib.parse import urlparse
    parsed_url = urlparse(next_url)
    
    if parsed_url.netloc in ALLOWED_HOSTS:
        # Redirect only to URLs that pass the host check
        return redirect(next_url)
    else:
        # If the host is not in the ALLOWED_HOSTS, abort the request
        abort(400, description="Unrecognized URL host.")

@app.route('/home')
def home():
    '''
    A default home page for demonstration purposes.
    '''
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run()