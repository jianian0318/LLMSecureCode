import os
from operator import itemgetter

def foo():
    return "./", "file.txt"

def dataSorting():
    '''
    Continuously take (basename,data) key-value pair from foo() function and sort it
    '''
    data_list = []
    while True:
        base, file = foo()
        data = os.path.join(base, file)
        
        # Generate key-value pair (basename, data)
        key_value = (os.path.basename(base), data)
        
        # Add the pair to the list
        data_list.append(key_value)
        
        # Condition to break the infinite loop can be added here (not included as not mentioned in comment)
        
    # Sort the list based on basename
    data_list.sort(key=itemgetter(0))
    return data_list