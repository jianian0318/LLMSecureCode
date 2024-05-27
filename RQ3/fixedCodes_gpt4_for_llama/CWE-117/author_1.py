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
    except ValueError:
        logging.error("Invalid input: %s. Please enter a valid number.", html.escape(user_input))
        converted_input = None
    return converted_input

if __name__ == "__main__":
    logging.basicConfig(filename="conversion_errors.log", level=logging.ERROR)
    converted_input = inputConversion()
    if converted_input is not None:
        print(f"The converted input is: {converted_input}")
    else:
        print("Invalid input. Please enter a valid number.")