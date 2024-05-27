from tempfile import NamedTemporaryFile


def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    with NamedTemporaryFile(mode='w', delete=False) as file:
        file.write(results)