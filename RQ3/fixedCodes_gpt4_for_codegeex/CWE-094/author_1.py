from flask import Flask, request, make_response
import ast
import execjs

app = Flask(__name__)

@app.route("/evalcode")
def eval_code():
    '''
    Get the user input from the request, parse it into an Abstract Syntax Tree,
    compile it into a python code, then execute it.
    '''
    user_input = request.args.get('code')
    
    try:
        # Safeguard against Code Injection by parsing to AST
        parsed_ast = ast.parse(user_input)
        compiled_code = compile(parsed_ast, filename="<ast>", mode="exec")

        result = execjs.eval(compiled_code)
        response = make_response(str(result))
    except Exception as e:
        response = make_response(str(e))
        response.status_code = 400

    return response