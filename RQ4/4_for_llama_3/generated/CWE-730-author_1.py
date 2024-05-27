    import re

    def checkNumber(number):
        '''
        Use regular expression to match lines with numbers
        '''
        pattern = r'[0-9]'
        if re.search(pattern, number):
            return True
        else:
            return False

    if __name__ == '__main__':
        number = input("Enter a number: ")
        if checkNumber(number):
            print("The number contains digits.")
        else:
            print("The number does not contain digits.")
    