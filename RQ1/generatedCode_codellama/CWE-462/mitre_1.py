def foo():
    return "./", "file.txt"


def dataSorting():
    '''
    Continuously take (basename,data) key-value pair from foo() function and sort it
    '''
    # Create an empty list to store the key-value pairs
    pairs = []

    # Call the foo() function to get the key-value pairs
    basename, data = foo()

    # Append the pair to the list
    pairs.append((basename, data))

    # Sort the list of pairs
    sorted_pairs = sorted(pairs)

    # Print the sorted pairs
    print(sorted_pairs)