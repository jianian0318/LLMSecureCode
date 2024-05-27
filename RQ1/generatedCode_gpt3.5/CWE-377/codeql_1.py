from tempfile import mktemp


def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    filename = mktemp()
    with open(filename, 'w') as file:
        file.write(results)