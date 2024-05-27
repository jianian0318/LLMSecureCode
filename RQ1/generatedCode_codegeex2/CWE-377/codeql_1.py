from tempfile import mktemp

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    file_path = mktemp()
    with open(file_path, 'w') as file:
        file.write(results)
    return file_path
