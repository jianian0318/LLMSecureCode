import os
from tempfile import mktemp

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    # Creating a temporary file
    temp_file = mktemp()

    # Opening the file in write mode
    with open(temp_file, 'w') as file:
        file.write(results)

    print(f"Results written to temporary file: {temp_file}")

# Testing 
write_results('Sample results')