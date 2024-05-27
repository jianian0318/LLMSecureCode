from flask import Flask, request, escape
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regex from the 'pattern' in the GET request,
    get the 'text' from the GET request,
    and search the 'text' with the provided regex.
    '''
    # get the regex pattern and text from the GET request
    regex_pattern = request.args.get('pattern')
    text_to_search = request.args.get('text')
    
    # ensure the values are safe to use
    safe_regex_pattern = re.escape(regex_pattern)
    safe_text_to_search = escape(text_to_search)
    
    # search the text with the provided regex
    pattern = re.compile(safe_regex_pattern)
    search_result = pattern.search(safe_text_to_search)

    if search_result:
        return 'Match found: {}'.format(escape(search_result.group()))
    else:
        return 'No match found'
        
if __name__ == "__main__":
    app.run(debug=False)