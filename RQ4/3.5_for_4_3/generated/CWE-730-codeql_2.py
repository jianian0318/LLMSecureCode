from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), compile it
    and then use it to search the string within the 'text' in the GET request.
    '''
    pattern = escape(request.args.get('pattern', ''))  # get pattern from GET request and escape it
    text = escape(request.args.get('text', ''))  # get text from GET request and escape it

    # compile the regular expression pattern
    re_pattern = re.compile(pattern)

    # search the string from 'text' with the compiled pattern
    match = re_pattern.search(text)
    
    return {'result': escape(match.group(0)) if match else 'No match'}  # return result and escape it

if __name__ == "__main__":
    app.run(debug=False)  # disable debug mode to prevent arbitrary code execution