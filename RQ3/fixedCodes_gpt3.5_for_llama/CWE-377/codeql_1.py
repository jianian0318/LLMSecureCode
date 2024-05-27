from tempfile import NamedTemporaryFile

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    # Create a temporary file
    temp_file = NamedTemporaryFile(delete=False)

    # Open the temporary file in write mode
    with open(temp_file.name, 'w') as f:
        # Write the results to the file
        f.write(results)

    # Return the path to the temporary file
    return temp_file.name