import tempfile

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    # Create a temporary file securely
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(results.encode())

    # Return the path of the temporary file
    return temp_file.name