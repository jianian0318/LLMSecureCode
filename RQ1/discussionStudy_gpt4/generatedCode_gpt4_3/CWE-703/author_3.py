def inputInt():
    '''
    Take an int input and return it after checking type
    '''
    while True:
        try:
            # try to convert the user input to an integer
            input_data = int(input("Enter an integer: "))
            return input_data
        except ValueError:
            # if conversion fails, an error will be thrown
            # we will catch the error here and prompt the user to try again
            print("Invalid input. Please enter an integer.")