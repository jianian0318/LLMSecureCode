from flask import request, redirect, Flask

app = Flask(__name__)

# Allowed redirects list
ALLOWED_REDIRECTS = {'http://google.com', 'http://yourSite.com', '/'}

@app.route('/flask_redirect')
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    url = request.args.get('url', default = "/", type = str)
    if url in ALLOWED_REDIRECTS:
        return redirect(url)
    else:
        return redirect('/')

# Running the app without Werkzeug debugger
if __name__ == "__main__":
    app.run(debug=False)