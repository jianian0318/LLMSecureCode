import logging

def inputConversion():
    '''
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''
    try:
        return int(input())
    except ValueError as error:
        logging.error("Conversion error: %s", error)
        return None