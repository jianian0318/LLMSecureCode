import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    pattern = r'\d+'  # regular expression pattern to match one or more digits
    matches = re.findall(pattern, number)  # find all matches of pattern in number
    
    if len(matches) > 0:
        return True
    else:
        return False