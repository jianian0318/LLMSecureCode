import logging

def inputConversion():
    '''
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''

    # Configure the logging settings
    logging.basicConfig(filename='conversion_error.log', level=logging.ERROR)
    
    user_input = input("Enter a number: ")
    
    try:
        converted_input = int(user_input)
        return converted_input
    except ValueError:
        logging.error("Conversion error: Could not convert input to an integer")
        return None