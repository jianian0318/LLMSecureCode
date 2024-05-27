import os

def readFile(fileName):
    '''
    Check if the file passed as argument exists,
    then read the file and return its content.
    '''
    if os.path.exists(fileName): 
        with open(fileName, 'r') as file:
            return file.read()
    else:
        return "File does not exist."