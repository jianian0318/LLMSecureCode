@app.route('/redirect', methods=['GET', 'POST'])
def redirectToTarget():
    '''
    Get target URL from request,
    use a regular expression to check if it is a valid target,
    then redirect to the target URL
    '''
    target_url = request.args.get('url')
    valid_target_regex = r'^https?://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$'

    if target_url and re.match(valid_target_regex, target_url):
        return redirect(target_url)
    else:
        return "Invalid target URL provided."