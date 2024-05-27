import os

def readFile(fileName):
    if os.path.exists(fileName):
        try:
            file = open(fileName, 'r')
            content = file.read()
            file.close()
            return content
        except:
            return None
    else:
        return None