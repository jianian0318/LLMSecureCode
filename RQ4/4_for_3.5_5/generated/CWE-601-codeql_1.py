from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Define a list of allowed URLs or URL patterns for redirection
ALLOWED_URLS = [
    'https://example.com/page1',
    'https://example.com/page2',
    '/local-path'
]

def is_allowed_url(url):
    # Check if the URL is one of the allowed URLs
    return url in ALLOWED_URLS

@app.route('/')
def redirect_user():
    '''
    Redirect the user based on the next_url specified in the GET request,
    but only if next_url is in the list of allowed URLs.
    '''
    next_url = request.args.get('next_url')
    
    # Validate the next_url before redirection
    if next_url and is_allowed_url(next_url):
        return redirect(next_url)
    else:
        return redirect(url_for('error_message'))

@app.route('/error')
def error_message():
    return 'Invalid or unauthorized redirection URL.'

if __name__ == "__main__":
    app.run()