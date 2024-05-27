from tempfile import NamedTemporaryFile

def write_results(results):
    '''
    Create a temporary file and write the results to it securely
    '''
    # Create a temporary file securely
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        # Write the results to the file
        temp_file.write(str(results))
        # Get the name of the temporary file
        temp_file_name = temp_file.name
    
    # Print the temporary file name
    print(f'The results have been written to temp file: {temp_file_name}')

# Example usage of the function:
write_results("Your results data here.")