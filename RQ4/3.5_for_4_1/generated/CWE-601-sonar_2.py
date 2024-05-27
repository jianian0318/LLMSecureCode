from flask import request, redirect, Flask
import urllib.parse

app = Flask(__name__)

@app.route('/flask_redirect')
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    url = request.args.get('url')  # Assuming the URL is provided as a query parameter

    if url:
        # Validate that the URL starts with 'http://' or 'https://'
        if url.startswith('http://') or url.startswith('https://'):

            # Validate the URL to prevent open redirection vulnerability
            parsed_url = urllib.parse.urlparse(url)

            # Check if the domain is in the whitelist
            if parsed_url.netloc and "example.com" in parsed_url.netloc:

                # Check if the URL path contains any dangerous characters
                if any(c in parsed_url.path for c in ['<', '>', "'", '"']):
                    return "Invalid URL provided for redirection.", 400

                return redirect(url)
            else:
                return "Invalid URL provided for redirection.", 400
        else:
            return "Invalid URL provided for redirection.", 400
    else:
        return "No URL provided for redirection.", 400

if __name__ == "__main__":
    app.run()