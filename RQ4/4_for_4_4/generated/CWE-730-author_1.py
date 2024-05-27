import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    # Compile a regular expression pattern that matches any sequence of digits
    pattern = re.compile(r'\d+')
    
    # Use re.search to check if the pattern is found within the input string 'number'
    if re.search(pattern, number):
        return True
    else:
        return False

# Example usage:
input_number = "This line contains the number 123."
print(checkNumber(input_number))  # Output: True, as the line contains '123'