from flask import Flask, redirect, request
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    target_url = request.args.get('url')
    if validateDomain(target_url):
        return redirect(target_url)
    else:
        return '<h1>Invalid Domain</h1>'

def validateDomain(url):
    if url is None:
        return False

    netloc = urlparse(url).netloc
    if netloc and netloc in ['www.valid-domain1.com', 'www.valid-domain2.com']:
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)