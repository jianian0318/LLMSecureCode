import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    pattern = r'\d+'  # regular expression pattern to match one or more digits
    matches = re.findall(pattern, number)  # find all matches of the pattern in the input string
    return bool(matches)  # return True if there is at least one match, False otherwise