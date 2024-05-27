from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('target')
    if target_url is None:
        return "No target URL provided", 400

    if not is_valid_domain(target_url):
        return "Invalid target URL", 400

    return redirect(target_url, code=302)

def is_valid_domain(url):
    # TODO: Implement domain validation logic
    return True

if __name__ == '__main__':
    app.run()
