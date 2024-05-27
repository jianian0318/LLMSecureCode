from flask import Flask, redirect, request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('url', None)

    if target_url is not None:
        # Parsing the URL for domain validation
        url_parts = urlparse(target_url)
        if url_parts.netloc:
            return redirect(target_url)
            
    return "Invalid or missing URL", 400

if __name__ == "__main__":
    app.run(debug=True)