def foo():
    return "./", "file.txt"


def dataSorting():
    '''
    Continuously take (basename,data) key-value pair from foo() function, sort by basename, and return the sorted list
    '''
    data = []
    while True:
      pair = foo()
      data.append(pair)
      data.sort(key=lambda x: x[0])
      yield data