from flask import Flask, redirect, request

app = Flask(__name__)

VALID_URLS = {"http://example.com", "https://example.com", "http://subdomain.example.com", "https://subdomain.example.com"}

@app.route('/redirect')
def redirectToTarget():
    """
    Securely redirects a user to a URL in a predefined list of allowed URLs.
    If the URL provided is not in the list, return an error message.
    """
    target_url = request.args.get('url')  # Get target URL from request
    # Validate the target URL
    if target_url in VALID_URLS:
        return redirect(target_url)  # Safely redirect to the target
    else:
        return 'Unauthorized URL'  # Display error for unauthorized URLs

if __name__ == "__main__":
    app.run(debug=False)  # Launch the server with debug mode disabled for production