from flask import Flask, redirect, request
import re

app = Flask(__name__)

@app.route('/redirect')
def redirectToTarget():
    target_url = request.args.get('target', '')
    if re.match(r'^https?:\/\/', target_url):
        return redirect(target_url)
    else:
        return "Invalid URL"

if __name__ == "__main__":
    app.run()