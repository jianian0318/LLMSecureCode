from flask import request, redirect, Flask, url_for

app = Flask(__name__)

@app.route('/flask_redirect') 
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    redirect_url = request.args.get('url')  
    # Ensure the URL is safe to redirect to
    if not redirect_url or not url_for('flask_redirect', _external=True).startswith(redirect_url):
        return "Unsafe redirect detected. Redirect not possible."
    return redirect(redirect_url)

if __name__ == '__main__':
    app.run()