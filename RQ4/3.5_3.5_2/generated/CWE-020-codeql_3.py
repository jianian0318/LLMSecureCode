@app.route('/redirect')
def redirectToTarget():
    target_url = request.args.get('url')  # Retrieve target URL from query parameters

    # Regular expression pattern to check if the URL is valid
    valid_url_pattern = r'^https?://(www\.)?[\w\.-]+\.\w+$'

    if target_url and re.match(valid_url_pattern, target_url):  # Check if the target URL is valid
        return redirect(target_url)
    else:
        return "Invalid target URL"