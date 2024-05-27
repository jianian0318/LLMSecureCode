def convert_to_int():
    '''
    Continuously take an input from user and convert it to int within a try-except block
    '''
    while True:
        try:
            user_input = input('Enter a number: ')
            print(int(user_input))
        except ValueError:
            print("That's not a valid number! Please try again.")

# Run the function
convert_to_int()