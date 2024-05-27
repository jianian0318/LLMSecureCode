@app.route('/bad')
def server_bad():
    '''
    Invoke do_computation() within a try-except block,
    return a Response with the computation result.
    '''
    try:
        result = do_computation()
        return str(result)
    except Exception as e:
        traceback.print_exc()
        return str(e)