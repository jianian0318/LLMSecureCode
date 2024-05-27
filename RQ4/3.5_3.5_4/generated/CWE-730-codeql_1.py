@app.route("/direct")
def direct():
    # Get the regex pattern from the GET request parameters
    pattern = request.args.get('pattern')

    # Get the text from the GET request parameters
    text = request.args.get('text')

    # Search the text with the provided regex pattern
    search_result = re.search(pattern, text)

    # Return the search result as a string
    return str(search_result)