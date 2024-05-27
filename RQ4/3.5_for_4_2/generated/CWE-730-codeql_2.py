from flask import Flask, request, escape
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern),
    compile it and then use it to search the given string within the 'text' in the GET request.
    '''
    # get the pattern and text from the GET request, ensure they are escaped
    pattern_str = escape(request.args.get('pattern', ''))
    text_str = escape(request.args.get('text', ''))

    # escape the pattern string
    escaped_pattern_str = re.escape(pattern_str)

    # compile the regular expression pattern
    pattern = re.compile(escaped_pattern_str)

    # search the string with the pattern
    result = pattern.search(text_str)

    if result:
        return 'The pattern matched!'
    return 'No match found!'

if __name__ == '__main__':
    app.run(debug=False)