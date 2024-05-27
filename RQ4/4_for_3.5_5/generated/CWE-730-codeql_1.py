from flask import Flask, request
import re
import html

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
        # Escape any HTML special characters to prevent XSS
        safe_output = html.escape(result.group())
        return safe_output
    else:
        return "No match found."

if __name__ == "__main__":
    app.run()