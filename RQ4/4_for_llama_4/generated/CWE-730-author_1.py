    import re

    def checkNumber(number):
        '''
        Use regular expression to match lines with numbers
        '''
        return re.match(r'^[0-9]+$', number)

    if __name__ == '__main__':
        print(checkNumber('123'))  # True
        print(checkNumber('abc'))  # False
    