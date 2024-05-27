def inputInt():
    '''
    Take an int input and return it after checking type
    '''
    while True:
        try:
            # Attempt to convert the user input to an integer
            user_input = input("Enter an integer: ")
            user_input = int(user_input)
            
            # If the conversion is successful, break the loop
            break
        except ValueError:
            # If the input was not able to be converted to an integer,
            # re-prompt the user
            print("Input must be an integer. Try again.")
    
    return user_input

inputInt()