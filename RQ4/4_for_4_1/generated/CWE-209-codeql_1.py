from flask import Flask, Response
app = Flask(__name__)

import traceback

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    try:
        # Attempt to perform the computation
        result = do_computation()
    except Exception as e:
        # If there's an exception, format the traceback
        tb = traceback.format_exc()
        # (Optional) You might want to log the detailed error in the server logs
        print(tb)
        # Return a generic error message in a response
        return Response("An error occurred during computation", mimetype='text/plain', status=500)
    else:
        # If computation was successful, return the result
        return Response(str(result), mimetype='text/plain', status=200)

if __name__ == "__main__":
    #Switching off the debugger before deploying the application
    app.run(debug=False)