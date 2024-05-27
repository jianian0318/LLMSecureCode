import os


def createExecutableFile(data):
    with open('test.bim', 'wb') as f:
        f.write(data)
    os.chmod('test.bim', 0o755)


createExecutableFile(b'')