import os

def readFile(fileName):
    '''
    Check if the file passed as argument exists,
    then read the file and return its content.
    '''
    if os.path.isfile(fileName):
        content = None
        with open(fileName, 'r') as file:
            content = file.read()
        return content
    else:
        return "File does not exist"