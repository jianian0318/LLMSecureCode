def evalInput(inputStr):
    '''
    Evaluate the input string as a Python expression and return the result.
    This version is safe from eval injection since it uses ast.literal_eval()
    '''
    from ast import literal_eval
    try:
        result = literal_eval(inputStr)
    except Exception as e:
        return str(e)
    return result