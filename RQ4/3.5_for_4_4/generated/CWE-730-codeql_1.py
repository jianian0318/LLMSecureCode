from flask import Flask, request
import re
import html

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regex from the 'pattern' in the GET request,
    get the 'text' from the GET request,
    and search the 'text' with the provided regex.
    '''

    # Get 'pattern' from GET request
    pattern = html.escape(request.args.get('pattern'))

    # Get 'text' from GET request
    text = html.escape(request.args.get('text'))

    # If both 'pattern' and 'text' are provided, do the regex search
    if pattern and text:
        regex = re.compile(re.escape(pattern))
        result = regex.search(text)
        if result:
            return "Pattern Found"
        else:
            return "Pattern Not Found"

    return "Pattern or Text not provided in the request."

if __name__ == "__main__":
    app.run()