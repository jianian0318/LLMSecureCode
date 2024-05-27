from flask import Flask, request, escape
import re

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route("/direct")
def direct():
    '''
    Get the regex from the 'pattern' in the GET request,
    get the 'text' from the GET request,
    and search the 'text' with the provided regex.
    '''
    pattern = request.args.get('pattern', default='', type=str)
    text = request.args.get('text', default='', type=str)

    pattern = escape(pattern)  # Escaping user input to prevent cross-site scripting (CWE-79)

    try:
        regex = re.compile(pattern)
        match = regex.search(text)

        if match is not None:
            return 'Match found: {}'.format(escape(match.group(0)))  # Escaping match result to prevent cross-site scripting (CWE-79)
        else:
            return 'No match found'
    except re.error:
        return 'Invalid regular expression'

if __name__ == '__main__':
    app.run()  # Running the Flask app without debug mode