import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    # Define a regular expression pattern to match any number (integer or float)
    pattern = re.compile(r'\d+\.?\d*')
    
    # Search the input string for the pattern
    if pattern.search(number):
        return True
    else:
        return False

# Example usage:
number_line = "This is a line with a number: 12345"
is_number_present = checkNumber(number_line)
print(is_number_present)  # Output should be True if a number is present