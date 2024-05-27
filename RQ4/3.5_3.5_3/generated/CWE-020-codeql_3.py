@app.route('/redirect', methods=['GET'])
def redirectToTarget():
    '''
    Get target URL from request,
    use a regular expression to check if it is a valid target,
    then redirect to the target URL
    '''
    target_url = request.args.get('url')
    # Assuming the regular expression pattern for a valid target URL
    pattern = re.compile('^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$')
    
    if pattern.match(target_url):
        return redirect(target_url)
    else:
        return 'Invalid target URL'