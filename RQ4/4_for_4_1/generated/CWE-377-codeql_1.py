from tempfile import mkstemp
import os

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    fd, temp_file = mkstemp()
    
    with os.fdopen(fd, 'w') as f:
        for result in results:
            f.write(str(result) + '\n')
    
    return temp_file