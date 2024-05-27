from flask import request, redirect, Flask

app = Flask(__name__)

# Define a whitelist of allowed URLs
ALLOWED_URLS = [
    "http://example.com",
    "https://www.example.org",
    "http://www.example.edu"
]

@app.route('/flask_redirect', methods=['GET'])
def flask_redirect():
    '''
    Get the url from the request, validate against a whitelist, and redirect if safe
    '''
    url = request.args.get('url')
    if url in ALLOWED_URLS:
        return redirect(url)
    # Optionally, redirect to a default page or show an error if URL is not allowed
    return "Unauthorized URL", 403

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)