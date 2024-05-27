from tempfile import mktemp


def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    # Create a temporary file
    temp_file = mktemp()

    # Open the temporary file in write mode
    with open(temp_file, 'w') as f:
        # Write the results to the file
        f.write(results)

    # Return the path to the temporary file
    return temp_file
