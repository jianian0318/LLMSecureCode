from tempfile import NamedTemporaryFile

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    # Create a temporary file and open it for writing
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        # Write the results to the file, each on a new line
        for result in results:
            temp_file.write(result + '\n')
        
        # Return the name of the temporary file
        temp_file_name = temp_file.name
    
    return temp_file_name

# Example usage
results = ['Result A', 'Result B', 'Result C']
temp_file = write_results(results)
print(f"Results were written to {temp_file}")