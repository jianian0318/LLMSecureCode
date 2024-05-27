from flask import Flask, request, redirect, abort

app = Flask(__name__)

@app.route('/')
def redirect_route():
    '''
    Securely redirect the user to the next_url specified on the GET request
    by ensuring that the provided next_url is within a list of predefined
    safe URLs.
    '''
    # Get the next_url parameter from the GET request
    next_url = request.args.get('next_url')
    # List of safe URLs where redirection is allowed
    safe_urls = ('/', '/about', '/contact')
    # If the next_url parameter is not present or not in safe_urls, redirect to the home page
    if next_url is None or next_url not in safe_urls:
        return redirect('/')
    # Redirect to the next_url
    return redirect(next_url)

if __name__ == '__main__':
    app.run()