def foo():
    return "./", "file.txt"

def dataSorting():
    '''
    Continuously take (basename,data) key-value pair from foo() function and sort it
    '''
    # Create an empty list to store the key-value pairs
    pairs = []

    while True:
        # Call the foo() function to get the key-value pairs
        basename, data = foo()

        # Check if the pair already exists in the list
        pair_exist = False
        for pair in pairs:
            if pair[0] == basename and pair[1] == data:
                pair_exist = True
                break

        # If the pair does not exist, append it to the list
        if not pair_exist:
            pairs.append((basename, data))

        # Sort the list of pairs
        sorted_pairs = sorted(pairs)

        # Print the sorted pairs
        print(sorted_pairs)