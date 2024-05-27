from flask import Flask, request
import re
import html

app = Flask(__name__)

@app.route("/direct")
def direct():
    # Get the regular expression pattern from the GET request (pattern)
    pattern = request.args.get('pattern', default=None)
    text = request.args.get('text', default='')

    # Check if the pattern is provided
    if pattern is None:
        return "Error: 'pattern' parameter is required."

    try:
        # Validate the pattern using regular expression escaping
        escaped_pattern = re.escape(pattern)

        # Compile the escaped pattern
        compiled_pattern = re.compile(escaped_pattern)

        # Use the compiled pattern to search the 'text'
        match = compiled_pattern.search(text)

        # If the match is found, return it, or return that no match was found
        if match:
            return {'match': html.escape(match.group())}
        else:
            return {'match': None}
    except re.error as e:
        # In case of an invalid regular expression pattern
        return "Error: Invalid regular expression pattern."

if __name__ == '__main__':
    app.run(debug=False)