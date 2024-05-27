import re


def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    pattern = r'^.*\b[0-9]+\b.*$'  # regular expression pattern to match lines with numbers
    if re.match(pattern, number):  # check if the number matches the pattern
        return True
    else:
        return False