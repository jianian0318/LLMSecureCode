import logging
import html

def inputConversion():
    '''
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''
    user_input = input("Enter a number: ")
    try:
        converted_input = int(user_input)
    except ValueError as e:
        sanitized_message = html.escape(str(e))
        logging.error(f"Conversion error: {sanitized_message}")
        return None
    return converted_input