from flask import Flask, request
import ast

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Get the user input from the request,
    parse it into an AST (Abstract Syntax Tree) representation,
    and evaluate it using the ast.literal_eval function.
    '''
    code = request.form['code']
    parsed_code = ast.parse(code, mode='eval')
    evaluated_code = ast.literal_eval(parsed_code.body)
    result = eval(evaluated_code)
    return "Code executed successfully"

if __name__ == "__main__":
    app.run()