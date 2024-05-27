from flask import request, redirect, Flask

app = Flask(__name__)

@app.route('/flask_redirect')
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    url = request.args.get('url', '') 
    return redirect(url, code=302)

if __name__ == "__main__":
    app.run(port=5000)