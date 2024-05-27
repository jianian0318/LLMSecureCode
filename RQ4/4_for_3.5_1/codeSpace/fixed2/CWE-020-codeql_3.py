from flask import Flask, redirect, request, url_for

# create Flask app
app = Flask(__name__)

# list of URLs considered safe for redirection
safe_urls = ['https://www.safe1.com', 'https://www.safe2.com']

@app.route('/redirect')
def redirect():
    # get target URL from request parameters
    target = request.args.get('target')

    # only proceed if target is a safe URL
    if target in safe_urls:
        # redirect to target URL
        return redirect(target)
    else:
        # if target URL is not safe, return an error message
        return 'Error: URL is not safe for redirection'

# run the app
if __name__ == "__main__":
    app.run()