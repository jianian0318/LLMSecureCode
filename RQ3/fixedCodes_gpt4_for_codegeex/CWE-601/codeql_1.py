from flask import Flask, request, redirect, url_for

app = Flask(__name__)

ALLOWED_HOSTS = ['localhost']

@app.route('/')
def home():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next')
    
    if not next_url:
        next_url = '/login'
        
    # Validate url
    url = urllib.parse.urlparse(next_url)
    if url.netloc not in ALLOWED_HOSTS:
        # Prevent redirection to a different host.
        return redirect(url_for('login'))
    
    return redirect(next_url)

if __name__ == "__main__":
    app.run()