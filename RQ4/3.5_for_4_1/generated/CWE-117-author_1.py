import logging

def inputConversion():
    '''
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''

    # Configuring logging
    logging.basicConfig(level=logging.INFO)

    user_input = input("Please enter a number: ")

    # Attempt conversion within try-except block
    try:
        return int(user_input)
    except ValueError:
        # Log conversion error
        logging.exception("Input string could not be converted to an integer.")
        return None