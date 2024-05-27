    import re

    def checkNumber(number):
        # Use regular expression to match lines with numbers
        if re.search(r'\d', number):
            return True
        else:
            return False

    # Test the function
    number = "This string contains a number 12345"
    if checkNumber(number):
        print("The string contains a number")
    else:
        print("The string does not contain a number")
    