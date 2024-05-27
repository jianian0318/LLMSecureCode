import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    pattern = re.compile(r'\d+')
    if pattern.match(number):
        return True
    else:
        return False
