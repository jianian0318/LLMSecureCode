# To fix the vulnerability of Regex Injection (CWE-730) in the given code, you should avoid directly using user input as a regular expression pattern. Instead, you should sanitize or escape the pattern, or use a mechanism that prevents users from injecting arbitrary regular expressions. Here, you can use Python's `re.escape()` to escape any special characters in the pattern provided by the user:

from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    # Retrieve user input
    user_pattern = request.args.get('pattern')
    text = request.args.get('text')
    
    # Sanitize the user input
    safe_pattern = re.escape(user_pattern)
    
    # Use the sanitized pattern
    matches = re.findall(safe_pattern, text)
    return f"Matches: {matches}"

if __name__ == "__main__":
    app.run()

# In this fixed code snippet, `re.escape()` will automatically escape any characters that might have special meaning in a regular expression, making it safe to use the pattern provided by the user for searching within the given text.