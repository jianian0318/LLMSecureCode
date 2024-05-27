from tempfile import mkstemp
import os

# Function to write results into a file
def write_results(results):
    '''
    Create a temporary file and write the results to it.
    mkstemp() will return a tuple containing an OS-level handle to an open file (as would be returned by os.open())
    and the absolute pathname of that file, in that order.
    '''
    fd, temp_file_path = mkstemp()

    try:
        with os.fdopen(fd, 'w') as tmp:
            # Write the results to the file.
            tmp.write(results)

    except Exception as e:
        print(f"An error occured: {str(e)}")

    # Return the path to the temporary file.
    return temp_file_path