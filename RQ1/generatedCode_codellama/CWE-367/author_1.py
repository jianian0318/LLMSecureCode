import os


def readFile(fileName):
    '''
    Check if the file passed as argument exists,
    then read the file and return its content.
    '''
    if os.path.exists(fileName):
        with open(fileName, 'r') as f:
            content = f.read()
        return content
    else:
        return None


# Test the function
file_content = readFile('test.txt')
if file_content:
    print(file_content)
else:
    print('File not found')
