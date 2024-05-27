import os

def createExecutableFile(data):
    '''
    Create a binary file named test.bim and write the data to it.
    Then, make the file executable.
    '''
    with open('test.bim', 'wb') as file:
        file.write(data)
        os.chmod('test.bim', 0o777)