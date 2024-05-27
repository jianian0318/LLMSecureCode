import tempfile

def write_results(results):
    '''
    Create a secure temporary file and write the results to it
    '''
    # Create a temporary file securely
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        # Write the results to the file
        temp_file.write(results)
        # Get the name of the temporary file
        temp_file_name = temp_file.name
    
    # Return the name of the temporary file
    return temp_file_name