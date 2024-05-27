from flask import request, redirect, Flask

app = Flask(__name__)


@app.route('/flask_redirect')
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    url = request.args.get('url')
    # Check if the URL starts with "http://" or "https://"
    if url.startswith('http://') or url.startswith('https://'):
        return redirect(url)
    else:
        return 'Invalid URL'


if __name__ == '__main__':
    app.run(debug=True)