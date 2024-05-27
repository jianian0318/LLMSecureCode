from flask import Flask, request
app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    user_input = request.form.get('user_input')
    try:
        code = compile(user_input, '<string>', 'exec')
        exec(code)
        return "Code executed successfully!"
    except Exception as e:
        return "An error occurred while executing the code: " + str(e)

if __name__ == "__main__":
    app.run()