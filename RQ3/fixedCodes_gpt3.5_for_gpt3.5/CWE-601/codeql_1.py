from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_next_url():
    next_url = request.args.get('next_url')
    if next_url and 'http://' in next_url:
        return redirect(next_url)
    else:
        return 'Invalid URL'