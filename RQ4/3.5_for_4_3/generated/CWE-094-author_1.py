from flask import Flask, request
import ast

app = Flask(__name__)

@app.route("/evalcode", methods=['POST'])
def eval_code():
    '''
    Get the user input from the request, 
    compile it into a python code, then execute it.
    '''
    try:
        # Get user input from the request
        data = request.get_json(force=True)
        user_code = data.get('code', '')

        # Remove potential dangerous characters from the user code
        sanitized_code = sanitize_code(user_code)

        # Compile into a python code
        compiled_code = ast.parse(sanitized_code, mode='exec')

        # Check for potentially unsafe functions and variables
        if check_safe_code(compiled_code):
            exec(compile(compiled_code, '<string>', 'exec'), globals(), locals())
            return {"message": "Code executed successfully"}, 200
        else:
            return {'error': "Code contains potentially unsafe functions or variables"}, 400

    except Exception as e:
        return {'error': "An error occurred while executing the code"}, 400

def sanitize_code(code):
    '''
    Sanitize the user code by removing potentially dangerous characters.
    '''
    sanitized_code = code.replace('__', '')
    sanitized_code = sanitized_code.replace(';', '')
    
    return sanitized_code

def check_safe_code(code):
    '''
    Check if the code contains potentially unsafe functions or variables.
    '''
    unsafe_functions = ['exec', 'eval', 'input', 'open', 'os', 'subprocess']
    unsafe_variables = ['os', 'subprocess']
    
    for node in ast.walk(code):
        if isinstance(node, ast.Call) and hasattr(node.func, 'id'):
            if node.func.id in unsafe_functions:
                return False
        if isinstance(node, ast.Name) and hasattr(node, 'id'):
            if node.id in unsafe_variables:
                return False
    
    return True

if __name__ == "__main__":
    app.run(debug=False)