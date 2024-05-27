import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    # Regular expression pattern for a number
    pattern = r'\b\d+\b'

    if re.fullmatch(pattern, number):
        return True
    else:
        return False