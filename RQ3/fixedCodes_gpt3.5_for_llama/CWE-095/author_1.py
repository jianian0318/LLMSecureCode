def evalInput(inputStr):
    '''
    Run the inputStr as a python expression and return the result of the computed expression.
    '''
    try:
        result = eval(inputStr)
    except Exception as e:
        result = "Invalid input: " + str(e)
    return result