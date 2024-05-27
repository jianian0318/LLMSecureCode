from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_next_url():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    return redirect(request.args.get('next_url'))