import tempfile

def write_results(results):
    '''
    Create a temporary file securely and write the results to it
    '''
    # Create a temporary file with a secure method
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        for result in results:
            temp_file.write(str(result) + '\n')  # Write each result to a new line in the file

    return temp_file.name  # Return the path of the temporary file