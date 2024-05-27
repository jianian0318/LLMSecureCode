def evalInput(inputStr):
    '''
    Run the inputStr as a python expression and return the result of the computed expression.
    '''
    import ast
    import operator as op

    operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
                 ast.Div: op.truediv, ast.USub: op.neg}

    def eval_(node):
        if isinstance(node, ast.Num): 
            return node.n
        elif isinstance(node, ast.BinOp):
            return operators[type(node.op)](eval_(node.left), eval_(node.right))
        elif isinstance(node, ast.UnaryOp):
            return operators[type(node.op)](eval_(node.operand))
        else:
            raise TypeError(node)

    try:
        inputStr = ast.parse(inputStr, mode='eval')
        result = eval_(inputStr.body)
    except:
        result = "Invalid input"
    return result