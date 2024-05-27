from flask import Flask, request, escape
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    # Get the regular expression pattern from the GET request (pattern)
    pattern = escape(request.args.get('pattern', default='.*', type=str))
    
    # Compile the regular expression pattern
    try:
        regex = re.compile(pattern)
    except re.error:
        return 'Invalid pattern. Please provide a valid regular expression.'
    
    # Get the 'text' from the GET request
    text = escape(request.args.get('text', default='', type=str))
    
    # Use the compiled pattern to search the provided 'text'
    match = regex.search(text)
    
    # If a match is found, return the matched string; otherwise, return 'No match'
    if match:
        return f'Match: {escape(match.group())}'
    else:
        return 'No match'

if __name__ == "__main__":
    app.run(debug=False)