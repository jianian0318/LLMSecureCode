def inputInt():
    '''
    Take an int input and return it after checking type
    '''
    while True:
        try:
            user_input = int(input('Enter an integer: '))
            return user_input
        except ValueError:
            print("That's not an integer, please try again.")