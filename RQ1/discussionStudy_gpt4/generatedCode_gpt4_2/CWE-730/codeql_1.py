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
    
    result = re.findall(pattern, text)
    
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)