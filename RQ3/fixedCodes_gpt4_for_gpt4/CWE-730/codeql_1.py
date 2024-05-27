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

    # Ensure pattern is only alphanumeric which prevents regex injection
    if not pattern.isalnum():
        return f"Error: Invalid pattern '{pattern}'. Pattern should be alphanumeric."

    # Ensure that the pattern is a valid regex
    try:
        regex = re.compile(pattern)
    except re.error:
        return f"Error: Invalid pattern '{pattern}'. Pattern is not a valid regex."

    search_result = regex.search(text)
    return f"The result of searching pattern '{pattern}' in text '{text}' is: {search_result.group() if search_result else 'No match'}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)