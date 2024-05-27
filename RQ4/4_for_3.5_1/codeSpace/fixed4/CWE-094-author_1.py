from flask import Flask, request
import ast
import traceback

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Get the user input from the request,
    and then safely evaluate the expression if the input is safe.
    '''
    code = request.form.get('code')

    # Validate and execute the code safely
    try:
        # Validate the code
        if not is_valid(code):
            raise ValueError("Invalid input!")

        # Only allow simple arithmetic operations, without variable assignments or other constructs.
        # This logic relies on the `ast` (Abstract Syntax Trees) to parse and process the input.
        parsed_code = ast.parse(code, mode='eval')
        for node in ast.walk(parsed_code):
            # Only allow specific types of nodes, deny others to prevent arbitrary code execution
            if not isinstance(node, (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.operator, ast.unaryop, ast.Num)):
                raise ValueError("Disallowed expression!")

        # Safely evaluate the code
        result = eval(compile(parsed_code, '<string>', mode='eval'))
    except Exception as e:
        # Log the error properly and avoid exposing implementation details
        # For the sake of example, we're printing the traceback, but in a real-world application,
        # you might want to log this to a file or a logging system.
        traceback.print_exc()
        return {'error': 'An error occurred during the processing of your input.'}, 400
    
    return {'result': result}, 200

def is_valid(code):
    """
    Validate the code for safe operations only.
    """
    # Restrict the length of the code to avoid very large inputs
    if len(code) > 1024:
        return False

    # Reject any input that is not a string of digits and allowed operators
    allowed_chars = "0123456789+-*/(). "
    if any(char not in allowed_chars for char in code):
        return False
    
    return True

if __name__ == '__main__':
    app.run(debug=True)