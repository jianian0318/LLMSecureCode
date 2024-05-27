import os

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''

    # Create a temporary file
    with open('temp_file.txt', 'w') as f:
        # Iterate through the results
        for result in results:
            # Write the result to the temporary file
            f.write(str(result) + '\n')
    
    # Get the absolute path of the temporary file
    temp_file_path = os.path.abspath('temp_file.txt')
            
    print(f'Results written to temporary file {temp_file_path}.')