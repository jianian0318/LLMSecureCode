import logging

def inputConversion():
    '''
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''
    
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    
    try:
        userInput = input("Please enter a number: ")
        convertedInput = int(userInput)
    except ValueError as e:
        logger.error("A conversion error occurred. Details : %s", str(e))
        return None
    else:
        return convertedInput