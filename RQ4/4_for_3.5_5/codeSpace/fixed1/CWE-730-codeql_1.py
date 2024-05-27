from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    
    # Escape the pattern to prevent ReDoS attacks
    escaped_pattern = re.escape(pattern)
    
    # Use the escaped pattern in search
    result = re.search(escaped_pattern, text)
    
    if result:
        return result.group()
    else:
        return "No match found."

if __name__ == "__main__":
    app.run()