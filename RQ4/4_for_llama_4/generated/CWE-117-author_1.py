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
        logging.error("Invalid input. Please enter a valid integer.")
        return None
    else:
        logging.info("Input conversion successful.")
        return converted_input

if __name__ == "__main__":
    inputConversion()