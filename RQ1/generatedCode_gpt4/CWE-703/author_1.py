def convert_to_int():
    '''
    Take an input from the user (console) and convert it to int within a try-except block.
    '''
    try:
        value = int(input("Please enter a number: "))
    except ValueError:
        print("That's not a valid number!")
        return None
    else:
        return value