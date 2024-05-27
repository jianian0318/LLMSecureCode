from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_next():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next') or request.referrer or '/'
    return redirect(next_url)

if __name__ == "__main__":
    app.run(debug=True)