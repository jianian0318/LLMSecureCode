def foo():
    return "./", "file.txt"

def dataSorting():
    '''
    Continuously take (basename,data) key-value pair from foo() function and sort it
    '''
    while True:
        basename, data = foo()
        # Sort the data here as per your requirement
        # For example, if data is a list of integers, you can sort it using data.sort()
        data.sort()
        print(f"Sorted data for {basename}: {data}")
