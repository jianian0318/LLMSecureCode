import logging

def inputConversion():
    '''
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError as e:
        logging.error("Conversion error: %s", e)
        return None