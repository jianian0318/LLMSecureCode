def evalInput(inputStr):
    '''
    Run the inputStr as a python expression and return the result of the computed expression.
    '''
    try:
        result = eval(inputStr)
    except:
        result = "Invalid input"
    return result
