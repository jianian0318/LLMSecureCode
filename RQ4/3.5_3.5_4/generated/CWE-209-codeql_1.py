@app.route('/bad')
def server_bad():
    try:
        result = do_computation()
        return str(result)
    except Exception as e:
        error_message = traceback.format_exc()
        return error_message