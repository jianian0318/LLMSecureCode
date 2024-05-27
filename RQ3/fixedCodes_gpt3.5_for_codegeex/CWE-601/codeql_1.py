from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_next_url():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next')
    if not next_url:
        next_url = '/login'
    return redirect(next_url)

if __name__ == '__main__':
    app.run()