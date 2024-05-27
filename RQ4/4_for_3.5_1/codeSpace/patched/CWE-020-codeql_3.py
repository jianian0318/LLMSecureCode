from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    target = request.args.get('target')
    if target is not None:
        if re.match('^https?://[^\s/$.?#].[^\s]*$', target):
            return redirect(target)
    
    return 'Invalid target URL'