import os

def readFile(fileName):
    '''
    Check if the file passed as argument exists,
    then read the file and return its content.
    '''
    try:
        with open(fileName, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return None

# Test the function
file_content = readFile('test.txt')
if file_content:
    print(file_content)
else:
    print('File not found')