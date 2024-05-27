from flask import Flask, Response
app = Flask(__name__)

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    '''
    Invoke do_computation() within a try-except block,
    return a Response with the computation result.
    '''
    try:
        # invoking the do_computation() function
        do_computation()
    except Exception as e:
        # Returning an error response without leaking sensitive information
        return Response("An error occurred", status=500)

if __name__ == '__main__':
    app.run()