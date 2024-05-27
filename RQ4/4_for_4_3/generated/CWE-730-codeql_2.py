from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), compile it
    and then use it to search the string within the 'text' in the GET request.
    '''

    # get pattern from request
    pattern = request.args.get('pattern')

    # escape special characters from pattern before compiling
    escaped_pattern = re.escape(pattern)
    
    # compile pattern
    regex = re.compile(escaped_pattern)

    # get text from request
    text = request.args.get('text')

    # find match
    match = regex.search(text)
   
    # return match as string
    return str(match)

if __name__ == "__main__":
    # Running the application without the debug mode
    app.run(debug=False)