from flask import Flask, redirect, request
from urllib.parse import urlparse

app = Flask(__name__)

ALLOWED_DOMAINS = ["example.com", "sub.example.com", "example.org"] 

@app.route('/redirect')
def redirectToTarget():
    
    target_url = request.args.get('url')
    if not target_url:
        return "No URL provided.", 400
        
    parsed_url = urlparse(target_url)
    if parsed_url.netloc not in ALLOWED_DOMAINS:
        return "Invalid or disallowed URL.", 400

    return redirect(target_url)

if __name__ == '__main__':
    app.run(debug=False)