from flask import request, redirect, Flask, url_for
from urllib.parse import urlparse, urljoin

app = Flask(__name__)

def is_safe_url(target):
    '''
    This function checks if the url is safe for redirection
    '''
    # Parse the host URL and the target URL.
    host_url = urlparse(request.host_url)
    redirect_url = urlparse(urljoin(request.host_url, target))

    # Validate that the target URL host is the same as the host URL's host.
    # This will prevent an attacker from supplying a URL that leads to a different domain.
    return (
        redirect_url.scheme in ('http', 'https') and
        host_url.hostname == redirect_url.hostname and
        host_url.port == redirect_url.port
    )

@app.route('/flask_redirect', methods=['GET'])
def flask_redirect():
    '''
    Get the url from the request and redirect to it if it is safe
    '''
    url = request.args.get('url')

    # Ensure that the URL exists in the request
    if url:
        # If the URL is safe for redirection, redirect to it.
        # Otherwise, return an error message.
        if is_safe_url(url):
            return redirect(url)
        else:
            return "URL is insecure. Please provide a secure URL."
    else:
        # If URL doesn't exist in the request, return an error message.
        return "URL is missing. Please provide URL."

if __name__ == "__main__":
    app.run(debug=False)  # Debug is set to false for security reasons