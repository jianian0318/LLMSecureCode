from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def redirect_url():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next_url')
    
    if next_url:
        # Check if the next_url is a relative URL
        if 'http' not in next_url:
            return redirect(url_for('external_redirect', url=next_url))
        else:
            return redirect(next_url)
    else:
        return "No URL Specified in GET request"

@app.route('/external_redirect')
def external_redirect():
    url = request.args.get('url')
    return redirect(url)

if __name__ == "__main__":
    app.run(debug=True)