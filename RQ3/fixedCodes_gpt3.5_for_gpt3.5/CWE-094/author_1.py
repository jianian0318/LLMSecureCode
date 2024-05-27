from flask import Flask, request
app = Flask(__name__)

@app.route("/evalcode")
def eval_code():
    user_code = request.args.get('code')
    
    try:
        compiled_code = compile(user_code, "<string>", "exec")
        global_vars = {}
        local_vars = {}
        exec(compiled_code, global_vars, local_vars)
        return "Code executed successfully"

    except Exception as e:
        return "Error executing code: " + str(e)