import tempfile

def write_results(results):
    '''
        Create a temporary file with UTF-8 encoding,
        write the unicode string results to it,
        and return its path.
    '''
    # Create a temporary file
    temp = tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8')

    # Write results to file
    temp.write(results)

    # Return path of the temporary file
    return temp.name
    temp.close()