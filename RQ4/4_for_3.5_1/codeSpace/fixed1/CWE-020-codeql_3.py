from flask import Flask, redirect, request

app = Flask(__name__)

# Maintained list of safe urls to allow redirection 
safe_urls = ['https://www.safe1.com', 'https://www.safe2.com']

@app.route('/redirect')
def redirectToTarget():
    target = request.args.get('target')
    if target is not None and target in safe_urls:
        return redirect(target)
    
    return 'Invalid target URL'