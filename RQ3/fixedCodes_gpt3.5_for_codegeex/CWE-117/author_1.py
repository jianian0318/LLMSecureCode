import logging


def inputConversion():
    user_input = input("Enter a number: ")
    try:
        converted_input = int(user_input)
    except ValueError as e:
        logging.error("Conversion error: %s", e)
        return None
    return converted_input