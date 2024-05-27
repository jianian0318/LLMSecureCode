from tempfile import mktemp

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    # Generate a unique temporary file name
    temp_file = mktemp()
    
    # Open the temporary file in write mode
    with open(temp_file, 'w') as file:
        # Write the results to the file
        file.write(results)
        
    # Return the name of the temporary file
    return temp_file