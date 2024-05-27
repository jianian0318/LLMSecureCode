from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Define a list of allowed URLs for redirection
ALLOWED_URLS = [
    'https://example.com/page1',
    'https://example.com/page2',
    '/local-path'
]

@app.route('/')
def redirect_user():
    '''
    Redirect the user based on the next_url specified in the GET request,
    but only if next_url is in the list of allowed URLs.
    '''
    next_url = request.args.get('next_url')
    
    # Validate the next_url
    if next_url in ALLOWED_URLS:
        return redirect(next_url)
    else:
        return redirect(url_for('error_message'))

@app.route('/error')
def error_message():
    return 'Invalid or unauthorized redirection URL.'

if __name__ == "__main__":
    app.run()