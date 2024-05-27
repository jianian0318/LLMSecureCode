from flask import Flask, request
import html
import re

app = Flask(__name__)

@app.route("/direct")
def direct():

    pattern_string = request.args.get('pattern')
    text = request.args.get('text')

    # Prevent CWE-79 cross-site scripting and CWE-117 regular expressions injection.
    # Use html.escape method to escape special HTML characters to prevent CWE-79 XSS.
    # Use re.escape method to escape special characters in the pattern string to prevent CWE-117
    escaped_pattern = re.escape(html.escape(pattern_string))
    escaped_text = html.escape(text)

    pattern = re.compile(escaped_pattern)
    match = pattern.search(escaped_text)

    if match is not None:
        return f"Matched: {match.group()}"
    else:
        return "Not Matched"

if __name__ == "__main__":
    # Prevent CWE-94 and CWE-215 by running app without debug mode.
    app.run(debug=False)