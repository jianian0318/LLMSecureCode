import os

def foo():
    return "./", "file.txt"

def dataSorting():
    '''
    Continuously take (basename,data) key-value pair from foo() function and sort it
    '''
    data_list = []
    while True:
        base, data = foo()
        data_list.append((os.path.basename(base), data))
        data_list.sort()
    return data_list