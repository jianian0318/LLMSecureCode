import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers.
    The function will return True if the entire string matches the pattern, otherwise it will return False.
    '''
    pattern = "^[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?$"
    if re.match(pattern, str(number)):
        return True
    return False