import os


def readFile(filename):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
            return content
        except IOError:
            return "Error while reading the file."
    else:
        return "File does not exist."