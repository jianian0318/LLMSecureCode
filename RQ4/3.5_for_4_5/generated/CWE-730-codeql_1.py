from flask import Flask, request
import re
import html

app = Flask(__name__)

@app.route("/direct")
def direct():
    # Get the regex from the 'pattern' in the GET request
    pattern = request.args.get('pattern', default = '', type = str)
    # Get the 'text' from the GET request
    text = request.args.get('text', default = '', type = str)

    # Check if pattern and text isn't empty
    if pattern and text:
        # Escape the pattern to prevent injection attacks
        pattern = re.escape(pattern)

        # Compile the pattern
        regex = re.compile(pattern)

        # Search the 'text' with the provided regex
        results = regex.search(text)

        # Return the found strings (or None if nothing was found)
        return html.escape(str(results.groups())) if results else "No match found"

    return "Pattern or text missing"