import logging

def inputConversion():
    user_input = input("Enter a number: ")
    try:
        converted_input = int(user_input)
        return converted_input
    except ValueError as e:
        logging.error(f"Conversion error: {e}")
        return None