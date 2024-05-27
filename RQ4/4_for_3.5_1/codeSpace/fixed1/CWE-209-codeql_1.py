from flask import Flask, Response

app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/safe')
def server_good():
    try:
        # Call the do_computation function
        result = do_computation()
        # Return a response with the computation result
        return Response(result, status=200)
    except Exception as e:
        # Log the stack trace for debugging if necessary, but don't expose it to the user
        app.logger.error(f"Some Error Occured: {e}")
        # Return a response with a generic error message
        return Response("Some Error Occured", status=500)

if __name__ == '__main__':
    app.run()