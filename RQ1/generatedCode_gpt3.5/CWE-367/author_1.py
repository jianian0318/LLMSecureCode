import os


def readFile(filename):
    '''
    Check if the file passed as an argument exists,
    then read the file and return its content.
    '''
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        return content
    else:
        return "File does not exist."