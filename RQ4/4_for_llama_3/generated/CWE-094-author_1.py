from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/displayinput")
def display_input():
    user_input = request.args.get('user_input')
    safe_user_input = escape(user_input)
    return "User input is: {}".format(safe_user_input)

if __name__ == "__main__":
    app.run(debug=False)