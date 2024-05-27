from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_next_url():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next_url')
    if next_url.startswith('http://') or next_url.startswith('https://'):
        return redirect(next_url)
    else:
        return "Invalid URL"