import os

def readFile(filename):
    '''
    Check if the file passed as an argument exists,
    then read the file and return its content.
    '''
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except IOError:
        return "File does not exist."