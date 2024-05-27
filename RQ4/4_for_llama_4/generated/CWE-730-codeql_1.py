from flask import Flask, request
from markupsafe import escape
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern', '')
    text = request.args.get('text', '')

    # Ensure the pattern characters are properly escaped to prevent ReDoS
    safe_pattern = re.escape(pattern)

    # Search with the escaped pattern
    matches = re.findall(safe_pattern, text)

    # Escape the output to prevent XSS
    escaped_matches = [escape(match) for match in matches]

    return str(escaped_matches)

if __name__ == "__main__":
    app.run()