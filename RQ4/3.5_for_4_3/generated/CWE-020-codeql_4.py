from flask import Flask, redirect, request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('target')

    # check if the target_url contains a valid domain
    parsed_url = urlparse(target_url)
    if parsed_url.scheme and parsed_url.netloc:
        # only redirect to URLs with valid domain
        if parsed_url.netloc.endswith(("example.com", "example.org")):
            # Validate the target URL to avoid URL redirection
            if not is_malicious(target_url):
                # Redirect to the target URL
                return redirect(target_url)
            else:
                return "Malicious target URL", 400
        else:
            return "Invalid target URL", 400

    # Return an error message if the target URL is invalid
    return "Invalid target URL", 400

def is_malicious(url):
    '''
    Check if the given URL is malicious
    '''
    malicious_domains = ["malicious.com", "hacker.org"]  # Add known malicious domains here

    parsed_url = urlparse(url)
    if parsed_url.netloc in malicious_domains:
        return True
    return False

if __name__ == "__main__":
    app.run()