import tempfile

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # Write the results to the temporary file
        temp_file.write(results.encode())
        # The file will be automatically deleted when it is closed, but we can also explicitly delete it using os.unlink()
    
    # Return the name of the temporary file
    return temp_file.name