import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    pattern = r"\b\d+\b"
    return bool(re.search(pattern, number))