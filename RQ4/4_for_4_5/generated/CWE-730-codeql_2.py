from flask import Flask, request
import re


app = Flask(__name__)


@app.route("/direct")
def direct():
    # Get the regular expression pattern from the GET request (pattern)
    pattern = request.args.get('pattern')
    # Get the text from the GET request
    text = request.args.get('text')
    
    # Ensure both pattern and text are provided
    if pattern is None or text is None:
        return "Pattern or text is missing in parameters", 400

    try:
        # Compile the regular expression pattern
        regex = re.compile(pattern)
    except re.error:
        return "Invalid regular expression pattern", 400

    # Use it to search the string within the 'text'
    match = regex.search(text)
    if match:
        # If a match is found, return the matched string
        return "Match found: " + match.group(), 200
    else:
        # If no match is found, inform the user
        return "No match found", 404


if __name__ == "__main__":
    app.run(debug=False)