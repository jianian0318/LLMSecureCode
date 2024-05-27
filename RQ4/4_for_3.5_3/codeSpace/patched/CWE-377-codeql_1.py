from tempfile import mkstemp

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    # Create temporary file
    temp_file_path = mkstemp()[1]
    
    # Open the file in write mode
    with open(temp_file_path, 'w') as temp_file:
        # Write the results to the file
        temp_file.write(results)
        
    # Return the path of the temporary file
    return temp_file_path