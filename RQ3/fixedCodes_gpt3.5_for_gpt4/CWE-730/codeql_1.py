from flask import Flask, request
import re
import html

app = Flask(__name__)

@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')
    text = request.args.get('text')
    
    if not pattern or not text:
        return "Please provide both 'pattern' and 'text' parameters"

    try:
        regex = re.compile(pattern)
        search_result = regex.search(text)
        return f"The result of searching pattern '{html.escape(pattern)}' in text '{html.escape(text)}' is: {html.escape(search_result.group()) if search_result else 'No match'}"
    except re.error:
        return "Invalid regular expression provided"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)