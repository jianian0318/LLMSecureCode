import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    pattern = r'\d+'  # define pattern to match one or more digits
    matched_lines = []

    # Iterate over each line in the input and check for a match
    for line in number.split('\n'):
        if re.search(pattern, line):
            matched_lines.append(line)

    return matched_lines