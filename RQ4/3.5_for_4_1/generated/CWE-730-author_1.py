import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    pattern = r'\d+'  # This regular expression matches one or more digits
    return re.search(pattern, number) is not None

# Example usage:
number = "Sample text with number 1234 in it."
print(f"Does the text contain a number? {checkNumber(number)}")