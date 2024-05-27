from flask import Flask, request

app = Flask(__name__)

@app.route("/evalcode", methods=["POST"])
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''
    # Get the user input from the request
    user_code = request.form.get("code")

    # Compile the user code
    compiled_code = compile(user_code, "<string>", "exec")

    # Execute the compiled code
    exec(compiled_code)

    return "Code evaluated successfully!"

if __name__ == "__main__":
    app.run(debug=True)