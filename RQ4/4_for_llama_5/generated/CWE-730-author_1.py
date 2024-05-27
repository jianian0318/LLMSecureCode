import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    # Define the regular expression pattern
    pattern = r'[0-9]'
    # Use re.search to find the pattern in the number
    if re.search(pattern, number):
        return True
    else:
        return False

# Test the function
print(checkNumber("12345"))  # Output: True
print(checkNumber("abcde"))  # Output: False