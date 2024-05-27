from flask import Flask, request
import ast

app = Flask(__name__)

@app.route('/evalcode', methods=['POST'])
def eval_code():
    try:
        # Get the expression from request
        expression = request.get_json().get('code')

        # Parse the expression safely as an AST node
        ast_node = ast.parse(expression, mode='eval')

        # Check if the parsed expression is of a safe type
        if not isinstance(ast_node.body, (ast.Expression, ast.Constant, ast.Num, ast.Str, ast.Bytes, 
                                          ast.NameConstant, ast.List, ast.Tuple, ast.Dict, ast.Set)):
            raise ValueError('Unsafe expression. Only literals are allowed.')

        # Compile and evaluate the safe expression
        # Use literal_eval for safety over eval
        result = ast.literal_eval(compile(ast_node, filename='<ast>', mode='eval'))

        return {'result': result}, 200

    except ValueError as e:
        # For security, obfuscate actual error details into a general error message
        return {'error': 'Unable to evaluate. Please provide a valid expression.'}, 400

    except Exception:
        # Catch all other exceptions and provide a generalized error message
        return {'error': 'Server error. Please try again later.'}, 500

# Never set the debug mode to True on production deployments!
if __name__ == "__main__":
    app.run(debug=False)