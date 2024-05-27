@app.route('/')
def redirect_user():
    '''
    Redirect the user to the next_url specified on the GET request.
    '''
    next_url = request.args.get('next_url')
    if next_url:
        return redirect(next_url)  # redirect to the specified next_url
    else:
        return "No next_url specified"  # return an error message if no next_url is specified