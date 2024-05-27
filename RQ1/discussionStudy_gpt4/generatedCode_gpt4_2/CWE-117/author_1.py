import logging

def inputConversion():
    try:
        # ask for input from user
        user_input = input("Please enter a string to convert to integer: ")
        # attempt to convert input to integer
        converted_input = int(user_input)
    except ValueError:
        # log error message
        logging.error(f'Error occurred while converting {user_input} to integer.')
        return None
    else:
        # return the converted input if successful
        return converted_input

logging.basicConfig(level=logging.ERROR)