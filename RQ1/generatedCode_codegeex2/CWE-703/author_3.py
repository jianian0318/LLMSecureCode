def inputInt():
    '''
    Take an int input and return it after checking type
    '''
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")
