import logging


def inputConversion():
    user_input = input("Enter a number: ")
    try:
        converted_input = int(user_input)
    except ValueError:
        logging.error("Invalid input. Please enter a valid number: %s", user_input)
        converted_input = None
    return converted_input


if __name__ == "__main__":
    logging.basicConfig(filename="conversion_errors.log", level=logging.ERROR)
    converted_input = inputConversion()
    if converted_input is not None:
        print(f"The converted input is: {converted_input}")
    else:
        print("Invalid input. Please enter a valid number.")