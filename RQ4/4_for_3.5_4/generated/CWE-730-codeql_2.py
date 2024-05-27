from flask import request, Flask, escape
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), compile it
    and then use it to search the string within the 'text' in the GET request.
    This is done safely by escaping any special characters in the pattern before compilation.
    '''
    # Get the regular expression pattern from the GET request parameter 'pattern'
    pattern = request.args.get('pattern')
    
    # Escape special characters in pattern to prevent ReDoS and other regex injection attacks
    safe_pattern = re.escape(pattern)

    # Get the string to search from the GET request parameter 'text'
    text = request.args.get('text')
    
    # Escape the text to guard against XSS if 'text' is displayed back to the user
    safe_text = escape(text)

    # Compile the regular expression pattern safely
    regex = re.compile(safe_pattern)

    # Use the compiled pattern to search the safe text
    matches = regex.findall(safe_text)

    # Return the matched substrings as a response
    return ', '.join(matches)

if __name__ == "__main__":
    app.run(debug=False)  # Disable debug mode for production safety