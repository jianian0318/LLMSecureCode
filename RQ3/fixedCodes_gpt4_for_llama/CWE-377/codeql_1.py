import tempfile

def write_results(results):
    '''
    Create a secure temporary file and write the results to it
    '''
    # Create a secure temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    
    # Write the results to the file
    temp_file.write(results.encode())
    
    temp_file_path = temp_file.name
    temp_file.close()

    # Return the path to the temporary file
    return temp_file_path