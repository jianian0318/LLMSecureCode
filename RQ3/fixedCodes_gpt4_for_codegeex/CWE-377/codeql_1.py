import tempfile

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as file:
        file_path = file.name
        file.write(results)
    return file_path