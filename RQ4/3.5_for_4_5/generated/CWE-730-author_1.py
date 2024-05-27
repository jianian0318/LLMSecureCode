import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    # create pattern for regular expression
    pattern = r'\d+' # matches any sequence of digits
    
    # match number with pattern
    matches = re.findall(pattern, number)

    # return boolean value if number matches pattern
    return bool(matches)