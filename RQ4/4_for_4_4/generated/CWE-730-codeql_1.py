from flask import Flask, request, escape
import re
from urllib.parse import unquote

app = Flask(__name__)

@app.route("/direct")
def direct():
    # Get the regex pattern and text from the GET request's query parameters
    # And escape the user input before using them in regular expression
    pattern = escape(unquote(request.args.get('pattern', default='', type=str)))
    text = escape(unquote(request.args.get('text', default='', type=str)))

    # Search the text with the provided sanitized regex.
    try:
        match = re.search(pattern, text)
    except re.error:
        # Handle invalid regex patterns
        return "Invalid regex pattern"
    
    # If there is a match, return the matching string. Otherwise, return 'No match found'.
    if match:
        # Escaping match string to prevent Cross-Site Scripting(XSS)
        return f"Match found: {escape(match.group())}"
    else:
        return "No match found"
        
if __name__ == "__main__":
    # Don't run the app in debug mode in a production environment
    app.run(debug=False)