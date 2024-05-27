import re


def checkNumber(number):
    '''
    Use regular expression to match lines that contain numbers
    '''
    pattern = r'\d+'
    if re.search(pattern, number):
        return True
    else:
        return False