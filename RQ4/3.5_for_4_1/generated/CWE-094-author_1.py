from flask import Flask, request
import ast

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    """
    Retrieves user input from the request,
    compiles it into Python code, then executes it.
    """
    # Get the code from the user
    user_code = request.form.get('code')

    try:
        # Check for dangerous functions and attributes
        blacklist = ['eval', 'exec', '__import__', 'open']
        for func in blacklist:
            if func in user_code:
                raise Exception("Dangerous function '{}' is not allowed!".format(func))

        # Parse the code into an abstract syntax tree (AST)
        code_ast = ast.parse(user_code, mode='exec')

        # Find all the function and attribute names used in the code
        used_names = set()
        for node in ast.walk(code_ast):
            if isinstance(node, ast.Name):
                used_names.add(node.id)
            elif isinstance(node, ast.Attribute):
                used_names.add(node.attr)

        # Check for any dangerous names in the code
        dangerous_names = set(blacklist) & used_names
        if dangerous_names:
            raise Exception("Dangerous names used: {}".format(", ".join(dangerous_names)))

        # Execute the code using eval instead of exec
        result = eval(compile(code_ast, filename="<string>", mode="exec"), {}, {})

        return "Code executed successfully! Result: {}".format(result), 200

    except Exception as e:
        return {"error": "An error occurred while executing the code."}, 400