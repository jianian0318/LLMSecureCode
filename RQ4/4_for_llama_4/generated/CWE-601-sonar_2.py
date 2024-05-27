from flask import request, redirect, Flask, url_for
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/flask_redirect')
def flask_redirect():
    url = request.args.get('url')
    netloc = urlparse(url).netloc
    if netloc == 'expected_website.com': # replace 'expected_website.com' with the actual expected URL
        return redirect(url)
    else: 
        return redirect(url_for('homepage')) # if the URL provided isn't as expected, redirect to homepage or an error page

@app.route('/homepage')
def homepage():
    return "This is homepage"

if __name__ == '__main__':
    app.run()