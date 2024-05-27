from flask import Flask, request
import re
import html

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), escape it,
    compile it, and then use it to search the string within the 'text' in the GET request.
    When returning matches, ensure to escape to prevent XSS in cases where output is rendered in HTML.
    '''
    # Get the regular expression pattern from the GET request parameter 'pattern'
    pattern = request.args.get('pattern', '')  # Default to empty string if not found
    # Get the string to be searched from the GET request parameter 'text'
    text = request.args.get('text', '')        # Default to empty string if not found

    # Escape any special characters in the user input pattern
    escaped_pattern = re.escape(pattern)

    # Compile the regular expression pattern
    regex = re.compile(escaped_pattern)

    # Use the regular expression pattern to search the string
    matches = regex.findall(text)

    # Escape output for safer HTML rendering
    safe_output = html.escape(str(matches))

    return safe_output

if __name__ == "__main__":
    app.run(debug=False)  # Turn off debug mode for production safety