import logging

def inputConversion():
    '''
    Take a string input from the user,
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''
    user_input = input("Enter a number: ")
    
    try:
        converted_input = int(user_input)
        return converted_input
    except ValueError as e:
        logging.error("Conversion error: {}".format(e))
        return None