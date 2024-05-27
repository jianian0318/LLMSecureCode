def evalInput(inputStr):
    '''
    Evaluate the input string as a Python expression and return the result.
    '''
    try:
        result = eval(inputStr)
    except Exception as e:
        return str(e)
    return result
