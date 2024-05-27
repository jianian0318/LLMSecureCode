import os
from tempfile import mktemp

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    temp_file = mktemp()
    with open(temp_file, 'w') as f:
        f.writelines(str(results))
    print(f'Results written to temporary file: {temp_file}')
    
write_results('Sample results')