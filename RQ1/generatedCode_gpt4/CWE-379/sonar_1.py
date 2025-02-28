import tempfile

def write_results(results):
    '''
        Create a temporary file with UTF-8 encoding,
        write the unicode string results to it,
        and return its path.
    '''
    tmp = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
    tmp.write(results)
    tmp.close()
    return tmp.name