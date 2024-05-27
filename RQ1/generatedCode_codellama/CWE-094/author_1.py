from flask import Flask, request
app = Flask(__name__)

@app.route("/evalcode")
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''
    user_input = request.args.get('user_input')
    code = compile(user_input, '<string>', 'exec')
    exec(code)
    return "Code executed successfully!"

if __name__ == "__main__":
    app.run()
