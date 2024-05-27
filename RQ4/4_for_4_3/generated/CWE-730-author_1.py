import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    The following regex pattern checks if the given string contains a number
    It searches for any sequence of digits in the string.
    '''
    pattern = r'\d+'  # This regex pattern looks for at least one or more digits
    match = re.search(pattern, number)
    return match is not None  # Return True if there is a match, else return False

# Example usage:
if checkNumber("There are 24 hours in a day."):
    print("The string contains a number.")
else:
    print("The string does not contain a number.")