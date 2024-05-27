from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), compile it
    and then use it to search the string within the 'text' in the GET request.
    '''
    # Obtain regular expression pattern from request
    pattern = request.args.get('pattern', default='.*', type=str)
  
    # Obtain search string from request
    text = request.args.get('text', default='', type=str)
    
    # Compile pattern and search in text
    compiled_pattern = re.compile(pattern)
    search_result = compiled_pattern.search(text)
  
    if search_result is None:
        return "No match found"
    else:
        return "Match found: {0}".format(search_result.group(0))
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)