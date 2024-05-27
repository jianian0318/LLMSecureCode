import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    pattern = r'\d+'  # Regular expression pattern to match numbers
    if re.match(pattern, number):
        return "Line contains number"
    else:
        return "Line does not contain number"

# Test the function
test_line1 = "This is a line without numbers"
test_line2 = "This line contains 123 numbers"
print(checkNumber(test_line1))
print(checkNumber(test_line2))