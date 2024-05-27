import logging

def inputConversion():
    '''
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    '''
    # get user input
    user_input = input("Enter a number: ")
    
    try:
        # attempt to convert user's input to an integer
        user_input = int(user_input)
    except ValueError:
        # log an error message if ValueError is raised
        logging.error("Invalid input, unable to convert to integer.")
        return None
    
    return user_input