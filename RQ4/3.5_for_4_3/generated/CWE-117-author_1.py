import logging

def inputConversion():
    '''
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''
    try:
        value = int(input("Please enter a number: "))
        return value
    except ValueError as e:
        logging.error('Error occurred: %s. User input could not be converted to an integer.', e)
        return None