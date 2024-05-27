from flask import Flask, request
import ast

app = Flask(__name__)

ALLOWED_AST_NODES = {
    'Module', 'Expr', 'Load', 'Num', 'Str', 'Name', 'BinOp', 'Add', 'Sub', 'Mult', 'Div', 'Pow', 'Mod', 'UnaryOp',
    'UAdd', 'USub', 'Compare', 'Lt', 'LtE', 'Gt', 'GtE', 'Eq', 'NotEq', 'List', 'ListComp', 'Set', 'SetComp', 
    'Dict', 'DictComp', 'Tuple', 'BoolOp', 'And', 'Or', 'Not', 'IfExp', 'Lambda', 'Call', 'Arg', 'For', 'While', 
    'If', 'With', 'AsyncWith', 'Await', 'Index', 'Slice', 'ExtSlice'
}

@app.route("/safecode", methods=["POST"])
def safe_eval_code():
    try:
        # Get the user input from the request
        user_input = request.get_json()["code"]

        # Transform it to the AST
        ast_module = ast.parse(user_input)

        for node in ast.walk(ast_module):
            if type(node).__name__ not in ALLOWED_AST_NODES:
                return {"result": "error", "message": "Unsupported operation."}, 400

        # AST Whitelist check would be here, e.g., to ensure only a limited set of operations are allowed.
        # Perform safe evaluation or handling logic here.

        return {"result": "success", "message": "Expression is within safe limits."}

    except Exception as _:
        # Do not leak information about the exception
        return {"result": "error", "message": "An error occurred during processing."}, 500

if __name__ == "__main__":
    app.run()