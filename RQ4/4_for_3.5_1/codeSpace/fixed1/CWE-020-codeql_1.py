from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request, make a response with it, and return it
    '''
    username = request.args.get('username')
    # sanitize user input
    esc_username = escape(username)
    response = make_response(esc_username)
    return response

if __name__ == '__main__':
    app.run()