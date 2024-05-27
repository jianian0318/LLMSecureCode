while True:
    try:
        user_input = input("Enter a number: ")
        converted_int = int(user_input)
        print("Converted to Integer:", converted_int)
    except ValueError:
        print("Please enter a valid integer.")