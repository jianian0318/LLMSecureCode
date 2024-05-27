@app.route('/bad')
def server_bad():
    try:
        do_computation() # invoke do_computation() within a try-except block
        return "Computation successful"
    except Exception as e:
        traceback.print_exc() # print the traceback to the console
        return "An error occurred"