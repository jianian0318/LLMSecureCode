from urllib.parse import urlparse
from flask import Flask, redirect, request, abort

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('url', None)
    if not target_url:
        abort(400, 'Missing URL parameter')

    parsed_url = urlparse(target_url)

    if bool(parsed_url.netloc) and bool(parsed_url.scheme):
        return redirect(target_url)
    else:
        abort(400, 'Invalid URL')

if __name__ == "__main__":
    app.run(debug=True)