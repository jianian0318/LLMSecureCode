import tempfile

def write_results(results):
    '''
    Create a secure temporary file and write the results to it
    '''
    with tempfile.NamedTemporaryFile(mode='w', delete=True) as file:
        file.write(results)
        file.seek(0)