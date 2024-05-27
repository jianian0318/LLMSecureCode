from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    if pattern and text:
        try:
            re.compile(pattern)
        except re.error:
            return "Invalid pattern"
        
        result = re.search(pattern, text)
        if result:
            return f"Match found: {result.group()}"
        else:
            return "No match found"
    else:
        return "Please provide both 'pattern' and 'text' in the GET request"

if __name__ == "__main__":
    app.run()