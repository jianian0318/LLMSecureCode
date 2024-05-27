import re


def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    # Use the re module to search for a pattern
    pattern = r'\d+'  # pattern to match any sequence of digits
    match = re.search(pattern, number)  # search for the pattern in the given string

    # Check if a match is found
    if match:
        return True
    else:
        return False