@app.route("/direct")
def direct():
    pattern = request.args.get('pattern')  # Get the regex from the 'pattern' parameter in the GET request
    text = request.args.get('text')  # Get the 'text' parameter from the GET request
    result = re.search(pattern, text)  # Search the 'text' with the provided regex
    return str(result) if result else "No match found"  # Return the search result as a string or "No match found" if there is no match