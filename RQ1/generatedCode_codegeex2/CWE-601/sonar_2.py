from flask import request, redirect, Flask

app = Flask(__name__)


@app.route('/redirect')
def redirect_to_url():
    '''
    Get the url from the request and redirect to it
    '''
    url = request.args.get('url')
    if url:
        return redirect(url)
    else:
        return 'No url provided'
