import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    pattern = "\d+"
    result = re.findall(pattern, str(number))
    return True if result else False