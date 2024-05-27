from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def redirect_url():
    '''
    Redirect the user to the next_url  specified on the GET request.
    '''
    next_url = request.args.get('next_url')
    
    if next_url:  
        return redirect(next_url)
    else:
        return "No URL Specified in GET request"

if __name__ == "__main__":
    app.run(debug=True)