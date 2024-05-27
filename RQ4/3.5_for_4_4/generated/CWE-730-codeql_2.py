from flask import Flask, request, escape
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    """
    Get the regular expression pattern from the GET request (pattern), compile it
    and then use it to search the string within the 'text' in the GET request.
    """
    # Get the pattern from the GET request
    pattern = escape(request.args.get('pattern'))

    # Get the text from the GET request
    text = escape(request.args.get('text'))

    # Escape the pattern before compiling the regular expression
    escaped_pattern = re.escape(pattern)

    try:
        # Compile the regular expression
        compiled_pattern = re.compile(escaped_pattern)

        # Search the pattern in the text
        match = compiled_pattern.search(text)

        # Return the matched groups if any
        return f"Matched Groups: {match.groups()}" if match else "No Match"
    except re.error:
        # Handle invalid regular expression patterns
        return "Invalid Regular Expression"

if __name__ == "__main__":
    app.run(debug=False)