def convert_to_int():
    '''
    Take an input from the user (console) and convert it to int within a try-except block.
    '''
    try:
        user_input = input("Please enter a number: ")
        print(int(user_input))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

convert_to_int()