from tempfile import NamedTemporaryFile

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    # Create a NamedTemporaryFile object
    temp_file = NamedTemporaryFile(delete=False)
    
    # Write the results to the temporary file
    with open(temp_file.name, 'w') as file:
        file.write(results)
    
    # Close the temporary file
    temp_file.close()
    
    # Return the name of the temporary file
    return temp_file.name