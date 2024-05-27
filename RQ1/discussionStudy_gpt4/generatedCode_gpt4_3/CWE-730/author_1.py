import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    pattern = r"\d+"
    return re.search(pattern, str(number)) is not None