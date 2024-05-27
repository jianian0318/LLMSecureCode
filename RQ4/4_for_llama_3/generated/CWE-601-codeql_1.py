import os
from flask import Flask, request, redirect, url_for, flash
from urllib.parse import urlparse, urljoin


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def home():
    return "Home Page"


@app.route('/redirect')
def redirecting_function():
    next_url = request.args.get('next')
    if not next_url:
        next_url = url_for('home')
    elif not is_safe_url(next_url):
        flash('The requested URL is not allowed.')
        next_url = url_for('home')
    return redirect(next_url)


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


if __name__ == '__main__':
    app.run(debug=True)