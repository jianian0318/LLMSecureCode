from tempfile import mktemp

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    temp_file = mktemp()  # Create a temporary file with a unique name
    with open(temp_file, 'w') as file:
        for result in results:
            file.write(str(result) + '\n')  # Write each result to a new line in the file
    return temp_file  # Return the path of the temporary file