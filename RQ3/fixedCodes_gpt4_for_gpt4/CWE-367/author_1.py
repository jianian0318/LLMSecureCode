import os

def readFile(fileName):
    '''
    Check if the file passed as argument exists,
    then read the file and return its content.
    '''
    try:
        with open(fileName, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File does not exist"