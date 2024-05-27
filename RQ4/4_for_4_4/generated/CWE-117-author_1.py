import logging

def inputConversion():
    '''
    Take a string input from the user,
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''
    # Create logger
    logger = logging.getLogger("Input Conversion Logger")
    logger.setLevel(logging.ERROR)

    # Create console handler and set its level to ERROR
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Add formatter to console handler
    console_handler.setFormatter(formatter)

    # Add console handler to logger
    logger.addHandler(console_handler)

    # Request user's input
    user_input = input("Please enter a number: ")

    try:
        # Attempt to convert the string to an integer
        converted_input = int(user_input)
    except ValueError as e:
        # Log a conversion error
        logger.error("Conversion error: Input is not a number. Retry with correct input.")
        return None

    return converted_input