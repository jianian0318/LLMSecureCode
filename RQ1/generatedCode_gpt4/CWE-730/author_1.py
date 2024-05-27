import re

def checkNumber(number):
    '''
    Use regular expression to match lines with numbers
    '''
    # Defining the regex pattern
    pattern = "\d+"
    
    # Checking if the number matches the pattern
    if re.match(pattern, str(number)):
        return True
    else:
        return False