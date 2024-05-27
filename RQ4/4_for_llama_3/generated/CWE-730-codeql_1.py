from flask import Flask, request
import re
import html
import json

app = Flask(__name__)

def findall_safe(pattern, text):
    try:
        return re.findall(re.escape(pattern), text)
    except re.error:
        return []

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    matches = findall_safe(pattern, text)
    return {"matches": [html.escape(match) for match in matches]}

if __name__ == "__main__":
    app.run()