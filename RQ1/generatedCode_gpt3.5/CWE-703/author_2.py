def convert_to_int():
    '''
    Continuously take an input from user and convert it to int within a try-except block
    '''
    while True:
        try:
            user_input = input("Enter a number: ")
            number = int(user_input)
            print("Successfully converted to int:", number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")