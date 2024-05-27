from tempfile import NamedTemporaryFile

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    # Create a temporary file
    temp_file = NamedTemporaryFile(delete=False)

    # Open the temporary file for writing
    with open(temp_file.name, 'w') as file:
        # Write the results to the file
        for result in results:
            file.write(str(result) + '\n')

    return temp_file.name