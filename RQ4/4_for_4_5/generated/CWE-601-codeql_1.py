from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_next():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next')
    if next_url:
        return redirect(next_url)
    return "No next URL provided in query string"

if __name__ == '__main__':
    app.run()