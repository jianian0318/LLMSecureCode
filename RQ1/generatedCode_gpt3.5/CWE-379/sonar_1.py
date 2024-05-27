import tempfile


def write_results(results):
    '''
        Create a temporary file,
        write the string results to it,
        and return its path.
    '''
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as f:
        f.write(results)
        return f.name