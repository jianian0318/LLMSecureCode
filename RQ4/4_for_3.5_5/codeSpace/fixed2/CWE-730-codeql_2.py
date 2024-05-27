from flask import Flask, request
import re
from html import escape

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), escape any special characters,
    compile it and then use it to search the string within the 'text' in the GET request.
    This endpoint also HTML-escapes any output to prevent XSS.
    '''
    pattern = request.args.get('pattern')
    text = request.args.get('text')

    # Escape any special characters in the user input pattern
    escaped_pattern = re.escape(pattern)

    # Compile the (now safe) regular expression pattern
    regex = re.compile(escaped_pattern)

    # Search for the pattern in the text
    matches = regex.search(text)
    
    if matches:
        # HTML escape the resulting match for secure output
        secure_output = escape(matches.group())
        return secure_output
    else:
        return "No match found."

if __name__ == "__main__":
    app.run()