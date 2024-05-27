def inputInt():
    '''
    Take an int input and return it after checking type
    '''
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")
