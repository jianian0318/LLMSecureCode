from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def redirect_user():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next')

    # Ensuring that it's a relative path in our webapp and not an arbitrary URL
    try:
        return redirect(url_for(next_url))
    except Exception:
        return "Wrong 'next' parameter provided in GET request. Unable to redirect."

if __name__ == '__main__':
    app.run(port=5000)  # run the application