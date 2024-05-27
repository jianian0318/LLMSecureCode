from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def redirect_user():
    '''
    Redirect the user to the next_url specified in the GET request.
    '''
    next_url = request.args.get('next_url')
    return redirect(next_url)