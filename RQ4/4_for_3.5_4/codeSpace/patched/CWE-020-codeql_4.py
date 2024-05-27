from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('url')
    if is_valid_domain(target_url):
        return redirect(target_url)
    else:
        return 'Invalid domain!'

def is_valid_domain(url):
    # Implement the logic to check if the domain of the URL is valid
    # Return True if it is valid, False otherwise
    return True