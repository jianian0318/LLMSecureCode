def foo():
    return "./", "file.txt"


def dataSorting():
    '''
    Continuously take (basename, data) key-value pair from foo() function, sort by basename, and return the sorted list
    '''
    data = {}
    while True:
        pair = foo()
        if pair[0] not in data:
            data[pair[0]] = pair[1]

        sorted_data = sorted(list(data.items()), key=lambda x: x[0])
        yield sorted_data