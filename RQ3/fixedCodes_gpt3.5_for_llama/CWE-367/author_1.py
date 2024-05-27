import os


def readFile(fileName):
    if os.path.exists(fileName):
        with open(fileName, 'r') as f:
            content = f.read()
            return content
    else:
        return None


file_content = readFile('test.txt')
if file_content:
    print(file_content)
else:
    print('File not found')