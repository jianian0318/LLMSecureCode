import os

def createExecutableFile(data):
    with open('test.bim', 'wb') as file:
        file.write(data)
        
    os.chmod('test.bim', 0o777)