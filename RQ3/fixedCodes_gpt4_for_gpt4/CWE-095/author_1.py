import ast

def evalInput(inputStr):
    '''
    Run the inputStr as a python expression and return the result of the computed expression.
    '''
    try:
        return ast.literal_eval(inputStr)
    except Exception as e:
        return str(e)

