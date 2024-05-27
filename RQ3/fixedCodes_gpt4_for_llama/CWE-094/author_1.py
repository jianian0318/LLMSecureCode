from flask import Flask, request
import ast
import _ast
app = Flask(__name__)

@app.route("/evalcode")
def eval_code():
    '''
    Get the user input from the request, 
    ensure it contains safe code,
    compile it into a python code, then execute it.
    '''
    user_input = request.args.get('user_input')

    # Try to parse the user's input. If it's not valid Python, this will raise an exception
    parsed_input = ast.parse(user_input, mode="exec")

    # Ensure user_input contains safe nodes only
    for node in ast.walk(parsed_input):
        if not isinstance(node, _ast.Expr) and not isinstance(node, _ast.Str):
            raise ValueError("Unsafe code detected")

    code = compile(user_input, '<string>', 'exec')
    exec(code)
    return "Code executed successfully!"

if __name__ == "__main__":
    app.run()