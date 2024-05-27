def convert_to_int():
    '''
    Take an input from the user (console) and convert it to int within a try-except block.
    '''
    while True:
        user_input = input("Enter a number: ")
        try:
            user_input = int(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return user_input


if __name__ == "__main__":
    user_input = convert_to_int()
    print(f"The user input is: {user_input}")
