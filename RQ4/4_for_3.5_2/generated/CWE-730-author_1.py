import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    # Create a regular expression pattern to match any line that contains a number
    pattern = r'\d+'

    # Use the re module's match function to check if the number matches the pattern
    if re.match(pattern, number):
        print("The number contains a line with a number")
    else:
        print("The number does not contain a line with a number")