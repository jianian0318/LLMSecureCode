from flask import request, redirect, Flask

app = Flask(__name__)


@app.route('/flask_redirect')
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    url = request.args.get('url')
    
    # Check if the url is safe and belongs to the same domain
    if url and 'example.com' in url:
        return redirect(url)
    else:
        return "Invalid URL"