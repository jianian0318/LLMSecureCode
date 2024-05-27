from flask import Flask, request
import re
import html

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), escape it,
    compile it, and then use it to search the string within the 'text' in the GET request.
    '''
    # Get the regular expression pattern from the GET request parameter 'pattern'
    pattern = request.args.get('pattern')
    # Get the string to be searched from the GET request parameter 'text'
    text = request.args.get('text')

    # Escape any special characters in the user input pattern
    escaped_pattern = re.escape(pattern)

    # Compile the regular expression pattern
    regex = re.compile(escaped_pattern)

    # Use the regular expression pattern to search the string
    matches = regex.findall(text)

    return str(matches)

if __name__ == "__main__":
    app.run(debug=True)