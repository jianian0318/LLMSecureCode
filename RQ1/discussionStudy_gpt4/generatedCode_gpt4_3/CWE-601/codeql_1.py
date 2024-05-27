from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/')
def redirect_user():
    '''
    Redirect the user to the next_url  specified on the GET request.
    '''
    next_url = request.args.get('next')
    if next_url:
        return redirect(next_url)
    else:
        return "No url provided"

if __name__ == "__main__":
    app.run(debug=True)