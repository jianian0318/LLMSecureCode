import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    # regular expression to match numbers
    pattern = "^[-+]?[0-9]*\.?[0-9]+$"
    
    # check if the input matches the pattern
    if re.match(pattern, str(number)):
        return True
    else:
        return False