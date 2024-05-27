import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    if re.search(r'\d', number):
        return True
    else:
        return False

# Test the function
print(checkNumber("This line contains a number 123"))  # Output: True
print(checkNumber("This line does not contain a number"))  # Output: False