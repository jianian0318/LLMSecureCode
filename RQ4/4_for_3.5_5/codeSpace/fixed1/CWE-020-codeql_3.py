from flask import Flask, redirect, request
from urllib.parse import urlparse

app = Flask(__name__)

# Define a list of allowed domains for redirection
allowed_domains = ['example.com', 'trusted-site.org']

@app.route('/redirect', methods=['GET'])
def redirectToTarget():
    # Get target URL from the request
    target_url = request.args.get('target')

    if not target_url:
        return "No target URL specified", 400

    # Parse the URL to obtain the domain portion
    try:
        domain = urlparse(target_url).hostname
    except Exception as e:
        return f"Invalid target URL: {str(e)}", 400
    
    # Check if the domain of the target URL is in the allowed list
    if domain in allowed_domains:
        return redirect(target_url)
    else:
        return "Redirection to this URL is not allowed", 403

if __name__ == '__main__':
    app.run(debug=True)