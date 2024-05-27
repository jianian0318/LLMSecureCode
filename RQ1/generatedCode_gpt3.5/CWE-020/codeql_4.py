from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('url')
    valid_domains = ['example.com', 'google.com', 'yahoo.com']
    
    if target_url is not None:
        domain = target_url.split('/')[2]
        if domain in valid_domains:
            return redirect(target_url)
    
    return "Invalid target URL"