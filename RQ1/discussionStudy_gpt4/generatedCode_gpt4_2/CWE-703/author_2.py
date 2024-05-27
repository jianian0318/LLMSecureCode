def convert_to_int():
    '''
    Continuously take an input from user and convert it to int within a try-except block
    '''
    while True:
        try:
            user_input = input("Please enter a number: ")
            integer = int(user_input)
            print("Converted to integer:", integer)
        except ValueError:
            print("Please enter a valid number")
            continue
convert_to_int()