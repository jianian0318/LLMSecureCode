import logging

def inputConversion():
    try:
        user_input = int(input("Enter a number: "))
        logging.info("Input converted to integer successfully")
        return user_input
    except ValueError:
        logging.error("Input could not be converted to integer")
        return None

# Example usage
result = inputConversion()
if result is not None:
    print("The converted input is:", result)
else:
    print("Invalid input")