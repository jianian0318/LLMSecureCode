def foo():
    # This function is supposed to return different key-value pairs over time.
    # For demonstration purposes, it will return one predefined pair, but in a practical
    # application this function would vary its output.
    return "./", "file.txt"


def dataSorting():
    '''
    Continuously take (basename, data) key-value pair from foo() function and sort it.
    To ensure no duplicate basenames are used, we'll check if the basename already exists 
    in our keys and update the data associated with it if it does.
    '''
    # Create an empty dictionary to store basename as keys and data as values
    unique_pairs = {}

    # Emulate continuously fetching data - for demonstration, we'll just call `foo` once
    basename, data = foo()

    # Use the basename as a key. If key already exists, it will update the value
    unique_pairs[basename] = data

    # Convert the dictionary items to a list of tuples and sort the list
    sorted_pairs = sorted(unique_pairs.items())

    # Print the sorted unique pairs
    print(sorted_pairs)


# Only call the dataSorting function if the script is executed as the main module
if __name__ == "__main__":
    dataSorting()