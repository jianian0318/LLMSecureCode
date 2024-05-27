import logging

def inputConversion():
    '''
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''
    
    try:
        # Take a string input from the user
        user_input = input("Please enter a number: ")

        # Convert it to an integer
        user_input = int(user_input)
        
    except ValueError:
        logging.exception("Failed to convert user input to an integer.")
    
    # Return the converted user input
    return user_input