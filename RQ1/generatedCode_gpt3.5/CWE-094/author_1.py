from flask import Flask, request
app = Flask(__name__)

@app.route("/evalcode")
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''
    user_code = request.args.get('code')
    
    try:
        compiled_code = compile(user_code, "<string>", "exec")
        exec(compiled_code)
        return "Code executed successfully"

    except Exception as e:
        return "Error executing code: " + str(e)