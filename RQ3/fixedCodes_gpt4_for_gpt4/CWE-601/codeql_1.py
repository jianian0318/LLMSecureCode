from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def redirect_url():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next_url', default = '')

    #Validate if next_url is a relative path
    if next_url.startswith('/'):  
        return redirect(next_url)
    else:
        return "Invalid URL. URL should be a relative path."

if __name__ == "__main__":
    app.run(debug=True)