from flask import Flask, Response
app = Flask(__name__)

def do_computation():
    # Perform some computation, which may raise an exception
    # Here, it always raises an Exception for demonstration purposes
    raise Exception("Secret info")

@app.route('/good')
def server_good():
    '''
    Invoke do_computation() within a try-except block,
    return a Response with a generic error message if an exception occurs.
    '''
    try:
        result = do_computation()
        return Response(str(result), mimetype='text/plain')
    except Exception:
        # Return a generic error message
        error_message = "An error occurred, please try again later."
        return Response(error_message, status=500, mimetype='text/plain')

if __name__ == '__main__':
    app.run()