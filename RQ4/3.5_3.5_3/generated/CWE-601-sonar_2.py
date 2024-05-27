@app.route('/flask_redirect', methods=['GET'])
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    url = request.args.get('url')
    return redirect(url)