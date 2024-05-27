from tempfile import mkstemp
import os


def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    # Generate a temporary file
    temp_path = mkstemp()[1]

    # Open the file with write permission
    with open(temp_path, 'w') as temp_file:
        # Write results to the file
        for result in results:
            temp_file.write(f"{result}\n")

    # Return the path of the temp file
    return temp_path