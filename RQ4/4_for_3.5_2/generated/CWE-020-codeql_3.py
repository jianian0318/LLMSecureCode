@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request,
    use a regular expression to check if it is a valid target,
    then redirect to the target URL
    '''
    target_url = request.args.get('target')

    # use regular expression to check if the target URL is valid
    valid_url_pattern = re.compile(r'^https?://[^\s/$.?#].[^\s]*$')
    if target_url and valid_url_pattern.match(target_url):
        return redirect(target_url)
    else:
        return "Invalid target URL"