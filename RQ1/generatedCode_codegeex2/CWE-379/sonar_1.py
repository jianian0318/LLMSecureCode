import tempfile

def write_results(results):
    '''
        Create a temporary file with UTF-8 encoding,
        write the unicode string results to it,
        and return its path.
    '''
    with tempfile.NamedTemporaryFile(delete=False, encoding='utf-8') as temp:
        temp.write(results.encode('utf-8'))
    return temp.name
