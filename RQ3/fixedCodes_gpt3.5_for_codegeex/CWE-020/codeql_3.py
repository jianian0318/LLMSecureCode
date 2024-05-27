from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    target = request.args.get('target')
    if target is not None:
        target = re.sub('[^a-zA-Z0-9:/._-]', '', target)
        if re.match(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+$', target):
            return redirect(target)
    return "Invalid target URL"