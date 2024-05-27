import logging

def inputConversion():
    user_input = input("Enter a number: ")
    try:
        converted_input = int(user_input)
        logging.info("Input converted to integer successfully.")
    except ValueError:
        logging.error("Input could not be converted to integer.")
        converted_input = None
    return converted_input

if __name__ == "__main__":
    logging.basicConfig(filename="input_conversion.log", level=logging.INFO)
    inputConversion()