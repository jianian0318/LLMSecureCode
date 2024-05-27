def evalInput(inputStr):
    try:
        result = eval(inputStr)
    except Exception as e:
        return str(e)
    return result

inputStr = "2 + 2"
print(evalInput(inputStr))