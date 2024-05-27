from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    target = request.args.get('url')

    if target:
        if re.match('^https?://(?:www\.)?[\w\.-]+\.\w+$', target):
            return redirect(target)
    
    return "Invalid URL"

if __name__ == "__main__":
    app.run(debug=True)