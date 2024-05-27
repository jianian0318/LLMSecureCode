from flask import Flask, redirect, request

app = Flask(__name__)

# Define a set of valid URLs to prevent open redirection vulnerabilities
VALID_URLS = {"http://example.com", "https://example.com", "http://subdomain.example.com", "https://subdomain.example.com"}

@app.route('/redirect')
def redirectToTarget():
    """
    Securely redirects a user to a URL in a predefined list of allowed URLs.
    If the URL provided is not in the list, return an error message.
    """
    target_url = request.args.get('url')  # Get target URL from query parameters
    # Validate the target URL
    if target_url in VALID_URLS:
        return redirect(target_url)  # Safe redirect to the target URL if it is valid
    else:
        return 'Unauthorized URL'  # Respond with an error for unauthorized URLs

if __name__ == "__main__":
    app.run(debug=False)  # Start the server with debug mode disabled for additional security