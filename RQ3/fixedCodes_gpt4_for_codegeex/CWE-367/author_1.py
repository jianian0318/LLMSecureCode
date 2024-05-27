import os

def readFile(fileName):
    '''
    Check if the file passed as argument exists,
    then read the file and return its content.
    TOCTOU race condition is avoided by using try and except. 
    The file is opened directly without checking its existence first.
    '''
    try:
        with open(fileName, 'r') as file:
            content = file.read()
        return content
    except IOError:
        return None