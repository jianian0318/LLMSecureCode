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
    if not target_url:
        return "Invalid Request. No URL found"

    # Parse the URL and examine the netloc property to make sure a domain is present
    parsed_url = urlparse(target_url)
    if not parsed_url.netloc:
        return "Invalid URL. No valid domain found"

    return redirect(target_url)

if __name__ == "__main__":
    app.run(debug=False)