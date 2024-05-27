from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/redirect', methods=['GET'])
def redirectToTarget():
    '''
    Get target URL from request, check if it contains a valid domain, and 
    then redirect to the target URL
    '''
    target_url = request.args.get('url')
    
    if target_url.startswith('http://') or target_url.startswith('https://'):
        return redirect(target_url)
    else:
        return 'Invalid URL'