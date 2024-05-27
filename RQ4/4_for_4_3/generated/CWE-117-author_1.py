import logging

def inputConversion():
    '''
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''
    # Create a logger
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)
    
    input_str_val = input("Please enter a value: ")
    
    try:
        # Attempt to convert the input to integer
        input_int_val = int(input_str_val)
    except ValueError as e:
        # Log the error message and raise it
        logger.error('Conversion error occurred: %s', str(e))
        raise
    else:
        # Return the converted value
        return input_int_val