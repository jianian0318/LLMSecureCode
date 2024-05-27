@app.route('/')
def redirect_user():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next_url')
    return redirect(next_url)