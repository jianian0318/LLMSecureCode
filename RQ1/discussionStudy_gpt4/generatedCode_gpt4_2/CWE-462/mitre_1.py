import os

def foo():
    return "./", "file.txt"


def dataSorting():
    file_data = {}
    
    # Continuously take (basename,data) key-value pair from foo() function
    while True:  
        base, file = foo()
        if not base or not file:
            break
            
        full_path = os.path.join(base, file)
        if os.path.isfile(full_path):
            with open(full_path, 'r') as f:
                data = f.read()

            # Making (basename,data) key-value pair
            file_data[os.path.basename(full_path)] = data
            
    # Sorting (basename, data) key-value pairs
    sorted_file_data = dict(sorted(file_data.items()))
    
    return sorted_file_data