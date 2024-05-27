def convert_to_int():
    '''
     continuously take an input from user and convert it to int within a try-except block
    '''
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            break
        except ValueError:
            print("Invalid input. Please try again.")
    return user_input
