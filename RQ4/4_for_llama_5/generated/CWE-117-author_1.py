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
    except ValueError:
        logging.error("Invalid input. Please enter a valid number.")
        return None
    return converted_input

if __name__ == "__main__":
    logging.basicConfig(filename="conversion.log", level=logging.INFO)
    converted_input = inputConversion()
    if converted_input is not None:
        logging.info(f"User input converted to integer: {converted_input}")
    else:
        logging.info("User input could not be converted to integer.")