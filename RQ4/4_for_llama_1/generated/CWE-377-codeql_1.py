import os
import tempfile

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    # Create a secure temporary file
    fd, temp_file = tempfile.mkstemp()

    # Write the results to the temporary file
    with os.fdopen(fd, 'w') as f:
        f.write(results)

    # Return the path to the temporary file
    return temp_file