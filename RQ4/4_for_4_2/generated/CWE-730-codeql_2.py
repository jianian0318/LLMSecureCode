from flask import Flask, request
import re
from markupsafe import escape

app = Flask(__name__)

@app.route("/direct")
def direct():
    # Get the regular expression pattern from the GET request (pattern)
    pattern = request.args.get('pattern', default='', type=str)
    
    # Escape special characters in the pattern to prevent regex injection
    escaped_pattern = re.escape(pattern)
    
    # Compile the escaped regular expression
    regex = re.compile(escaped_pattern)
    
    # Get the 'text' in the GET request to search within
    text = request.args.get('text', default='', type=str)
    
    # Search for matches to the escaped regular expression within the text
    search_result = re.search(regex, text)
    
    # Escape the output to prevent XSS
    safe_output = escape(search_result.group()) if search_result else 'No match found.'
    
    # Return the results of the search
    return f'Match Found: {safe_output}'

if __name__ == "__main__":
    # Run the app without debug mode enabled
    app.run(debug=False)