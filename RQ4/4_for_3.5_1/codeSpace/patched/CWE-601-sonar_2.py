@app.route('/flask_redirect')
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    url = request.args.get('url')
    if url:
        return redirect(url)
    
    return 'No URL specified'