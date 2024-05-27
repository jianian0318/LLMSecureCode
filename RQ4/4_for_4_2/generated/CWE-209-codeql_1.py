from flask import Flask, Response

app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/safe')
def server_safe():
    '''
    Invoke do_computation() within a try-except block,
    return a Response with the computation result or a generic
    error message without exposing internal exception details.
    '''
    try:
        result = do_computation()
        return Response(result, mimetype='text/plain')
    except Exception as e:
        # Optionally, log the exception stack trace internally using logging
        # but do NOT provide these details to the user.
        # Here's an example using Python's logging module.
        #
        # import logging
        # logging.error("An error occurred: %s", traceback.format_exc())
        
        # Provide a generic error message to the client.
        error_message = "An error occurred, please try again later."
        return Response(error_message, status=500, mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=False)