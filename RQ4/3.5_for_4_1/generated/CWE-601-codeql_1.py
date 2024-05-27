from flask import Flask, request, redirect, urljoin, abort

app = Flask(__name__)

@app.route('/')
def redirect_user():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next_url') # get the next_url from the GET request
    if next_url:
        # Validate the next_url to prevent URL redirection based on unvalidated user input
        parsed_url = urljoin(request.url_root, next_url)
        if parsed_url.startswith(request.url_root) and parsed_url != request.url_root: # Check if the parsed_url starts with the request.url_root
            return redirect(parsed_url) # redirect to the parsed URL
        else:
            abort(400, "Invalid URL.")
    else:
        return "No URL to redirect."


if __name__ == "__main__":
    app.run() # Run the Flask app without debug mode