import os

def foo():
    return "./", "file.txt"

def dataSorting():
    '''
    Continuously take (basename,data) key-value pair from foo() function and sort it
    '''
    data_dict = {}
    while True:
        base, data = foo()
        data_dict[os.path.basename(base)] = data
        sorted_data = sorted(data_dict.items())
    return sorted_data