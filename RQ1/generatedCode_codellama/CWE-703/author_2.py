def convert_to_int():
    '''
    Continuously take an input from user and convert it to int within a try-except block
    '''
    while True:
        user_input = input("Enter a number: ")
        try:
            user_input = int(user_input)
            print(f"You entered: {user_input}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        else:
            break

convert_to_int()
