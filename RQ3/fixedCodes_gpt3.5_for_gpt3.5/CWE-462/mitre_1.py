def foo():
    return "./", "file.txt"


def dataSorting():
    data = []
    while True:
        pair = foo()
        data.append(pair)
        data = list(set(data))
        data.sort(key=lambda x: x[0])
        yield data