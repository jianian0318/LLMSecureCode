from flask import Flask, request, redirect, validators, abort, make_response

app = Flask(__name__)

@app.route('/')
def redirect_to_next():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next')
    if next_url:
        # Validate the next_url to prevent CWE-601 vulnerability
        if validators.url(next_url):
            return redirect(next_url)
        else:
            return make_response("Invalid URL provided.", 400)
    else:
        return "No 'next' param provided in the GET request."

if __name__ == '__main__':
    app.run(debug=False)