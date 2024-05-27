from flask import Flask, request
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regex from the 'pattern' in the GET request,
    get the 'text' from the GET request,
    and search the 'text' with the provided regex.
    '''
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    
    # Escape the pattern to prevent injection and ReDoS attacks
    safe_pattern = re.escape(pattern)
    
    matches = re.findall(safe_pattern, text)
    return str(matches)

if __name__ == "__main__":
    app.run(debug=True)