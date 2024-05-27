from flask import Flask, redirect, request
import re

app = Flask(__name__)


@app.route('/redirect')
def redirectToTarget():
    target_url = request.args.get('target')
    pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )
    if target_url and pattern.match(target_url):
        return redirect(target_url)
    else:
        return "Invalid or missing target URL"

if __name__ == "__main__":
    app.run()