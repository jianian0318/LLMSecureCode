from flask import request, redirect, Flask

app = Flask(__name__)

@app.route('/flask_redirect')  
def flask_redirect():
    redirect_url = request.args.get('url')  
    if redirect_url.startswith('http://') or redirect_url.startswith('https://'):
        return redirect(redirect_url)
    else:
        return 'Invalid URL format'

if __name__ == '__main__':
    app.run()