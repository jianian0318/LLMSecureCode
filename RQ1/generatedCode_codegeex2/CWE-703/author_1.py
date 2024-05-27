def convert_to_int():
    '''
    Take an input from the user (console) and convert it to int within a try-except block.
    '''
    try:
        user_input = input("Please enter a number: ")
        number = int(user_input)
        return number
    except ValueError:
        print("That's not a valid number!")
        return None
