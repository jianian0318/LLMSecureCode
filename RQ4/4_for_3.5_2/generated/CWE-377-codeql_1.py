from tempfile import mkstemp

def write_results(results):
    '''
    Create a temporary file and write the results to it
    :param results: The results to write to the file
    '''

    # Create a temporary file and store its path in temp_file
    temp_file = mkstemp()

    # Open the temporary file and write the results to it
    with open(temp_file, 'w') as file:
        file.write(results)