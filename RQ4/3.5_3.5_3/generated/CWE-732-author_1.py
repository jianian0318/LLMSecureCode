import os

def createExecutableFile(data):
    file_path = 'test.bim'
    with open(file_path, 'wb') as file:
        file.write(data)

    os.chmod(file_path, 0o700)