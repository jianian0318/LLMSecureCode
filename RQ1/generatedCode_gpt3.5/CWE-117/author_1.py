import logging


def inputConversion():
    '''
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''
    try:
        user_input = input("Enter a number: ")
        converted_input = int(user_input)
        return converted_input
    except ValueError:
        logging.error("Conversion Error: Invalid input. Please enter a valid number.")